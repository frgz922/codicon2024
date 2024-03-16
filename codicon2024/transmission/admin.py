from django.contrib import admin
from .models import Transmission, Categoria,  Tags

# Register your models here.
admin.site.register(Transmission)
admin.site.register(Categoria)
admin.site.register(Tags)