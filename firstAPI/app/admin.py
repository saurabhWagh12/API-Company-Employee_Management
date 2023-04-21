from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','type']

# Register your models here.
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee)