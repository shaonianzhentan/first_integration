from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([MyBinarySensor(hass, config_entry)])

class MyBinarySensor(BinarySensorEntity):

    def __init__(self, hass, config_entry):
        self._attr_should_poll = False
        self._attr_unique_id = f'{config_entry.entry_id}-binary_sensor'
        self._attr_name = '人在传感器'
        self._attr_device_class = BinarySensorDeviceClass.MOTION
        self._attr_device_info = DeviceInfo(
            identifiers={('first_integration', config_entry.entry_id)},
            manufacturer="制造商",
            model="模型",
            name='我的设备',
            sw_version='1.0',
        )
        # 自定义属性
        self._attr_extra_state_attributes = {
            'attr1': 'value1',
            'attr2': 'value2',
        }

        hass.bus.async_listen("switch_update_event", self.async_update_data)

    async def async_update_data(self, event):
        self._attr_is_on = event.data.get('state')
        self.schedule_update_ha_state()