from django.contrib import admin
from .models import Profile, Image, option

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(option)
