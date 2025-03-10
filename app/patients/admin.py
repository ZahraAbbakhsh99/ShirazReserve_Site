from django.contrib import admin
from .models import Patient


# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'insurance_type', 'national_id', 'gender', 'phone_number']
    search_fields = ('first_name', 'last_name', 'national_id', 'phone_number')
    list_filter = ('insurance_type', 'gender')
    fields = ('first_name', 'last_name', 'insurance_type', 'national_id', 'gender', 'phone_number')
