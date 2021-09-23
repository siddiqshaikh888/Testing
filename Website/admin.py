from django.contrib import admin

# Register your models here.
from .models import Website

admin.site.register(Website)

from .models import Selldata

admin.site.register(Selldata)