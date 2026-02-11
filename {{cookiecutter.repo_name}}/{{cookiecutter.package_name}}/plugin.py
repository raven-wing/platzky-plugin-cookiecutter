"""{{ cookiecutter.description }}"""

from typing import cast

from platzky.engine import Engine
from platzky.plugin.plugin import PluginBase, PluginBaseConfig


class {{ cookiecutter.plugin_class_name }}Config(PluginBaseConfig):
    """Configuration model for the {{ cookiecutter.plugin_class_name }} plugin."""

    pass


class {{ cookiecutter.plugin_class_name }}Plugin(PluginBase[{{ cookiecutter.plugin_class_name }}Config]):
    """Platzky {{ cookiecutter.plugin_class_name }} plugin."""

    @classmethod
    def get_config_model(cls) -> type[{{ cookiecutter.plugin_class_name }}Config]:
        """Return the config model class for this plugin."""
        return {{ cookiecutter.plugin_class_name }}Config

    def process(self, app: Engine) -> Engine:
        """Process the app with this plugin's configuration."""
        config = cast({{ cookiecutter.plugin_class_name }}Config, self.config)
        return app
