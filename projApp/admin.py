from django.contrib import admin
# from .models import *
from django.apps import apps


# Register your models here.


# admin.site.register(Patient, Physician)
# admin.site.register(Schedule, MedicalRecord)
# admin.site.register(DeviceData, Consultation)

#automate registration of models as they're added
collect_models = apps.get_app_config('projApp').get_models()

for model in collect_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
