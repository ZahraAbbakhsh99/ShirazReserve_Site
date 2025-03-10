from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True


# Create your models here.
class Doctor(models.Model):
    # user = models.OneToOneField( User, on_delete=models.CASCADE, related_name='doctor_profile')
    first_name = models.CharField(null=False, blank=False, unique=False, max_length=100, verbose_name="First Name")
    last_name = models.CharField(null=False, blank=False, unique=False, max_length=150, verbose_name="Last Name")
    medical_code = models.CharField(null=False, blank=False, unique=True, primary_key=True, max_length=5,
                                    verbose_name="Medical Code")
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    specialty = models.CharField(null=False, blank=False, unique=False, max_length=100, verbose_name="Specialty")
    description = models.TextField(blank=True, null=True, unique=False, verbose_name="Description")
    phone_number = models.CharField(null=False, blank=True, max_length=11, verbose_name="Phone Number")
    clinic_addresses = models.CharField(max_length=500, verbose_name="Clinc Address")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"دکتر {self.first_name} {self.last_name} _ {self.specialty}"

    class Meta:
        db_table = 'doctors'
        verbose_name = "doctor"



