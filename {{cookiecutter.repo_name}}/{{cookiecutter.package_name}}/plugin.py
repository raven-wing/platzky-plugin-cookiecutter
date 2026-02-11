from typing import cast

from platzky.plugin.plugin import PluginBase, PluginBaseConfig


class {{ cookiecutter.plugin_class_name }}Config(PluginBaseConfig):
    pass


class {{ cookiecutter.plugin_class_name }}Plugin(PluginBase[{{ cookiecutter.plugin_class_name }}Config]):
    @classmethod
    def get_config_model(cls) -> type[{{ cookiecutter.plugin_class_name }}Config]:
        return {{ cookiecutter.plugin_class_name }}Config

    def process(self, app):
        config = cast({{ cookiecutter.plugin_class_name }}Config, self.config)
        return app
