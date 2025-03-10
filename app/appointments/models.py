from django.db import models
from django.core.exceptions import ValidationError
from doctors.models import Doctor
from patients.models import Patient
from times.models import DoctorTime


# Create your models here.
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Patient")
    time = models.ForeignKey(DoctorTime, on_delete=models.CASCADE, verbose_name="datetime")
    clinc_address = models.CharField(null=True, blank=True, max_length=255, verbose_name="Clinc Address")

    def clean(self):
        try:
            doctor_datetime = self.time.get(
                doctor=self.doctor,
                doctor_date__date=self.time.doctor_date.date,
                time=self.time,
                available=True
            )
        except DoctorTime.DoesNotExist:
            raise ValidationError("The selected date and time is not available for this doctor.")

        if doctor_datetime.available:
            doctor_datetime.available = False
            doctor_datetime.save()
        else:
            raise ValidationError("This time slot is already taken.")

    def __str__(self):
        return f"نوبت برای {self.patient.__str__()} با {self.doctor.__str__()}" \
               f" در {self.time.doctor_date.date} _ {self.time}"

