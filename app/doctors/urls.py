from django.urls import path
from .views import *

urlpatterns = [
    path('doctor_details/<str:medical_code>/', doctor_detail_view, name='doctor_details'),
]