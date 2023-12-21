from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.components.select import SelectEntity

from datetime import datetime

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([MySelect(config_entry)])


class MySelect(SelectEntity):

    def __init__(self, config_entry):
        self._attr_unique_id = f'{config_entry.entry_id}-select'
        self._attr_name = '事件订阅'
        self._attr_current_option = None
        self._attr_options = [
            '取消订阅',
            '单次订阅',
            '持续订阅',
        ]
        # 取消订阅的临时变量
        self._unsubscribe = None

    async def async_select_option(self, option: str) -> None:
        self._attr_current_option = option

        # 取消订阅事件
        if self._unsubscribe is not None:
            self._unsubscribe()
            self._unsubscribe = None

        if option == '单次订阅':
            self._unsubscribe = self.hass.bus.async_listen_once(
                'subscription_testing', self.async_subscription_testing_once)
        elif option == '持续订阅':
            self._unsubscribe = self.hass.bus.async_listen(
                'subscription_testing', self.async_subscription_testing)

    async def async_subscription_testing_once(self, event):
        print('单次订阅', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self._unsubscribe = None
        
    async def async_subscription_testing(self, event):
        print('持续订阅', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))