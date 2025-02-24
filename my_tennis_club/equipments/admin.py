from django.contrib import admin
from .models import Equipment
# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')

admin.site.register(Equipment, EquipmentAdmin)