from django.contrib import admin
from app1.models import Bangalore_jobs,Bihar_jobs,Hydrabad_jobs
# Register your models here.

class Bang(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']


admin.site.register(Bangalore_jobs,Bang)

class Bihar(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']

admin.site.register(Bihar_jobs,Bihar)

class Hydra(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']

admin.site.register(Hydrabad_jobs,Hydra)