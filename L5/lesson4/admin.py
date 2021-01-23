from django.contrib import admin
from . import models
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_rec', 'price', 'u_measure', 'name_provider']


admin.site.register(models.Products, ProductsAdmin)
