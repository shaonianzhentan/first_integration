from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.const import Platform

DOMAIN = 'first_integration'

PLATFORMS = (
    # Platform.ALARM_CONTROL_PANEL,
    Platform.BINARY_SENSOR,
    # Platform.BUTTON,
    # Platform.CALENDAR,
    # Platform.CAMERA,
    # Platform.CLIMATE,
    # Platform.COVER,
    # Platform.DATE,
    # Platform.DATETIME,
    # Platform.DEVICE_TRACKER,
    # Platform.EVENT,
    # Platform.FAN,
    # Platform.HUMIDIFIER,
    # Platform.IMAGE,
    # Platform.LAWN_MOWER,
    # Platform.LIGHT,
    # Platform.LOCK,
    # Platform.MEDIA_PLAYER,
    # Platform.NUMBER,
    # Platform.REMOTE,
    # Platform.SCENE,
    Platform.SELECT,
    Platform.SENSOR,
    # Platform.SIREN,
    # Platform.STT,
    Platform.SWITCH,
    # Platform.TEXT,
    # Platform.TIME,
    # Platform.TTS,
    # Platform.VACUUM,
    # Platform.UPDATE,
    # Platform.WAKE_WORD,
    # Platform.WATER_HEATER,
    # Platform.WEATHER,
  )

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)

    async def send_message(call: ServiceCall):
        data = call.data
        await hass.services.async_call('persistent_notification', 'create', {
            'title': data.get('entity_id'),
            'message': data.get('message')
        })

    hass.services.async_register(DOMAIN, "send_message", send_message)
    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    return await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
