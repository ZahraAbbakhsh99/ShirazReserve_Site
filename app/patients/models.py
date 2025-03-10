from django.db import models
from django.core.exceptions import *

# Create your models here.
class Patient(models.Model):
    class InsuranceType(models.TextChoices):
        SOCIAL_SECURITY = ('تامین', "تامین اجتماعی")
        HEALTH_SERVICES = ('سلامت', "خدمات درمانی")
        FREE = ('آزاد', "آزاد")

    GENDER_CHOICES = [
        ('زن', "زن"),
        ('مرد', "مرد"),
    ]

    first_name = models.CharField(blank=False, null=False, unique=False, max_length=100, verbose_name="First Name")
    last_name = models.CharField(null=False, blank=False, unique=False, max_length=150, verbose_name="Last Name")
    insurance_type = models.CharField(null=True, blank=True, max_length=10, choices=InsuranceType.choices, default=InsuranceType.FREE,
                                      verbose_name="Insurance Type")
    national_id = models.CharField(null=False, blank=False, unique=True, primary_key=True, max_length=10,
                                   verbose_name="National ID")
    gender = models.CharField(null=True, blank=True, max_length=6, choices=GENDER_CHOICES, verbose_name="Gender")
    phone_number = models.CharField(null=False, blank=True, max_length=11, verbose_name="Phone Number")

    def __str__(self):
        prefix = ''
        if self.gender == 'زن':
            prefix = "خانم"
        elif self.gender == 'مرد':
            prefix = "آقا"
        return f" {prefix} {self.first_name} {self.last_name}_ ({self.national_id})"

    def clean(self):
        super().clean()
        if not self.national_id.isdigit() or len(self.national_id) != 10:
            raise ValidationError("کد ملی باید 10-رقم باشد.")
        if not self.phone_number.isdigit() or len(self.phone_number) != 11:
            raise ValidationError("شماره همراه باید 11-رقم باشد.")






