from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.components.binary_sensor import BinarySensorEntity

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([MyBinarySensor(hass)])

class MyBinarySensor(BinarySensorEntity):

    def __init__(self, hass):
        self._attr_should_poll = False
        hass.bus.async_listen("switch_update_event", self.async_update_data)

    async def async_update_data(self, event):
        self._attr_is_on = event.data.get('state')
        self.schedule_update_ha_state()