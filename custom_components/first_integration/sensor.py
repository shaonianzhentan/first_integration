from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.components.sensor import SensorEntity

from datetime import datetime
from pytz import timezone

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([MySensor()])

class MySensor(SensorEntity):

    def __init__(self):
        pass
    
    async def async_update(self):
        self._attr_native_value = datetime.now(timezone(self.hass.config.time_zone))
