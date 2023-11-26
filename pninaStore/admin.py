from django.contrib import admin
from .models import *


class categoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields if field.name not in ('id', 'qual_key', 'qual_desc')]


class productAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields if field.name not in ('id', 'qual_key', 'qual_desc')]


class supplierAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Supplier._meta.fields if field.name not in ('id', 'qual_key', 'qual_desc')]


class orderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields if field.name not in ('id', 'qual_key', 'qual_desc')]


admin.site.register(Category, categoryAdmin)
admin.site.register(Product, productAdmin)
admin.site.register(Supplier, supplierAdmin)
admin.site.register(Order, orderAdmin)
