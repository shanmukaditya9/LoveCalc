from django.contrib import admin
from .models import Store_Data

# Register your models here.
class Data_Layout(admin.ModelAdmin):
    list_display = ['name1','db1','name2','db2','result']

admin.site.register(Store_Data,Data_Layout)