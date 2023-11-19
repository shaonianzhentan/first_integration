from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = 'first_integration'

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    return True
