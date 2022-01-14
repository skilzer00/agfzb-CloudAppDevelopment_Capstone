from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name',  'dealer_id', 'year', 'car_type']
    search_fields = ['name']


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    search_fields = ['name']


admin.site.register(CarModel)
admin.site.register(CarMake, CarMakeAdmin)