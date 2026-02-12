from unittest.mock import MagicMock

from {{ cookiecutter.package_name }}.plugin import {{ cookiecutter.plugin_class_name }}Plugin


def test_process_returns_app():
    app = MagicMock()
    plugin = {{ cookiecutter.plugin_class_name }}Plugin({})
    result = plugin.process(app)
    assert result is app
