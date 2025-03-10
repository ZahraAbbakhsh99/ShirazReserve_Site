from django.urls import path
from .views import *

urlpatterns = [
    path('reserve/', reservation_view, name='patient_reservation'),
]
