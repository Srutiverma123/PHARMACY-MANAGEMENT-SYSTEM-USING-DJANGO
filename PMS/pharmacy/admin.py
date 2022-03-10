#To add Medicine from models.py such that admin has rights to add,delete and update the medicne details

from django.contrib import admin #importing admin.py
from .models import Medicine #importing Medicine from models.py

admin.site.register(Medicine)