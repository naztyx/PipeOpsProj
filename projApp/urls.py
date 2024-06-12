from django.urls import path

from .views import *

urlpatterns = [
    path('', signin_signup, name='authenticate'),
    path('home_dashboard/', home_dashboard, name='index'),
    path('update_medical_record/', update_medical_record, name='update_medical_record')
]