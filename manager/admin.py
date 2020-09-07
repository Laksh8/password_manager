from django.contrib import admin
from .models import Detail
# Register your models here.

def Register(model):
    return admin.site.register(model)

Register(Detail)