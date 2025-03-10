from django.db import models
from doctors.models import Doctor
from ShirazReserve.utils import jalali_converter, jalali_converter_with_hour


# Create your models here.
class DoctorDate(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor")
    date = models.DateField(verbose_name="date")

    class Meta:
        unique_together = ('doctor', 'date')
        verbose_name = "Date"

    def __str__(self):
        return f"{self.doctor.__str__()} - {self.date}"

    @property
    def jalali_date(self):
        return jalali_converter(self.date)


class DoctorTime(models.Model):
    doctor_date = models.ForeignKey(DoctorDate, on_delete=models.CASCADE, verbose_name="DoctorDate")
    time = models.TimeField(verbose_name="time")
    available = models.BooleanField()

    class Meta:
        verbose_name = "Time"

    def __str__(self):
        return f"{self.doctor_date.date} ({self.time})"

    @property
    def jalali_time(self):
        return jalali_converter_with_hour(self.time)
