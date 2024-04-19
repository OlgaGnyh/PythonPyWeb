from django.contrib import admin
from .models import TypeTrans, TypeVehicle, Carriers, Routes

admin.site.register(TypeTrans)
admin.site.register(TypeVehicle)
admin.site.register(Carriers)
admin.site.register(Routes)

