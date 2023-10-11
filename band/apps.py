from django.apps import AppConfig


class BandConfig(AppConfig):
    """
       Configuration class for the 'band' app.

       This class represents the configuration for the 'band' app within a Django project.
       It specifies the default auto field for model creation and the name of the app.

       Attributes:
       default_auto_field (str): The name of the default auto field to use for model creation.
       name (str): The name of the 'band' app.

       Example:
       ```
       from django.apps import apps

       band_app = apps.get_app_config('band')
       print(f"App name: {band_app.name}")
       print(f"Default auto field: {band_app.default_auto_field}")
       ```
       """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'band'
