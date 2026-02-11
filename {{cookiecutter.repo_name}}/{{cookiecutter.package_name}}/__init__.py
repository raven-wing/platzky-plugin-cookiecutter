from {{ cookiecutter.package_name }}.plugin import {{ cookiecutter.plugin_class_name }}Plugin

Plugin = {{ cookiecutter.plugin_class_name }}Plugin

__all__ = [
    "Plugin",
    "{{ cookiecutter.plugin_class_name }}Plugin",
]
