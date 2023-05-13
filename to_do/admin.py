from django.contrib import admin

# Register your models here.
from .models import to_do

admin.site.register(to_do)
