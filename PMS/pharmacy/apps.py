#Naming the application
from django.apps import AppConfig

class PharmacyConfig(AppConfig): #cretaed automatically when command `python manage.py startapp pharmacy` is used
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pharmacy' #application name
