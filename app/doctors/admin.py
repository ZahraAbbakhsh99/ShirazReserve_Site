from django.contrib import admin
from .models import Doctor


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'medical_code', 'phone_number', 'image',)
    search_fields = ('first_name', 'last_name', 'specialty', 'medical_code', 'phone_number',)
    list_filter = ('specialty',)
    fieldsets = (
        ('Information', {
            'fields': ('first_name', 'last_name', 'specialty', 'medical_code', 'phone_number', 'image', 'description')
        }),
        ('Clinc Information', {
            'fields': ('clinic_addresses',)
        }),
    )


admin.site.register(Doctor, DoctorAdmin)

