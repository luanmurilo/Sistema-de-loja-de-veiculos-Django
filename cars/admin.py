from django.contrib import admin
from cars.models import Car
from cars.models import Brand 

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'plate', 'photo')
    search_fields = ('model',) 

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)   
admin.site.register(Car, CarAdmin)