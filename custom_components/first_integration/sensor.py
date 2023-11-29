from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.helpers.device_registry import DeviceInfo

from homeassistant.components.sensor import SensorEntity, SensorDeviceClass

from datetime import datetime
from pytz import timezone

from random import randint

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([MySensor(config_entry), TemperatureSensor(config_entry)])

class MySensor(SensorEntity):

    def __init__(self, config_entry):
        # 设置唯一ID
        self._attr_unique_id = f'{config_entry.entry_id}-timestamp'
        # 设置传感器名称
        self._attr_name = '时间传感器'
        # 设置传感器图标
        self._attr_icon = 'mdi:home-assistant'
        # 设置设备类别
        self._attr_device_class = SensorDeviceClass.TIMESTAMP
        # 设置设备信息
        self._attr_device_info = DeviceInfo(
            identifiers={('first_integration', config_entry.entry_id)},
            manufacturer="制造商",
            model="模型",
            name='我的设备',
            sw_version='1.0',
        )
    
    async def async_update(self):
        self._attr_native_value = datetime.now(timezone(self.hass.config.time_zone))

class TemperatureSensor(SensorEntity):

    def __init__(self, config_entry):
        # 设置唯一ID
        self._attr_unique_id = f'{config_entry.entry_id}-temperature'
        # 设置传感器名称
        self._attr_name = '温度传感器'
        # 设置设备类别
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        # 设置传感器单位
        self._attr_native_unit_of_measurement = '°C'
        # 设置设备信息
        self._attr_device_info = DeviceInfo(
            identifiers={('first_integration', config_entry.entry_id)},
            manufacturer="制造商",
            model="模型",
            name='我的设备',
            sw_version='1.0',
        )

    async def async_update(self):
        # 随机设置0到100的数字
        self._attr_native_value = randint(0, 100)