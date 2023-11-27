from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.components.switch import SwitchEntity


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([MySwitch()])

class MySwitch(SwitchEntity):

    def __init__(self):
        pass
    
    async def async_update(self):
        pass
    
    async def async_turn_on(self, **kwargs):
        ''' 打开 '''
        self._attr_is_on = True
        self.hass.bus.fire('switch_update_event', { 'state': self._attr_is_on })
    
    async def async_turn_off(self, **kwargs):
        ''' 关闭 '''
        self._attr_is_on = False
        self.hass.bus.fire('switch_update_event', { 'state': self._attr_is_on })