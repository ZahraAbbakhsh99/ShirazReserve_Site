from django.urls import path
from .views import *

urlpatterns = [
    path('report/<int:time_id>/', report_view, name='report_view'),
    path('tracking/<int:national_id>', tracking_view, name='tracking_view'),
]
