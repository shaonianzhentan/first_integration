import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from . import DOMAIN

class ConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None, errors=None):
        
        if user_input is not None:
            return self.async_create_entry(title="我的集成", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            errors=errors,
        )