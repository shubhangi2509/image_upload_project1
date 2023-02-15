from django.contrib import admin
from .models import Image

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','title','image']

admin.site.register(Image,ImageAdmin)