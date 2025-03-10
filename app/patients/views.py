from django.shortcuts import render
from patients.models import Patient
from appointments.models import *
from times.models import DoctorTime, DoctorDate


# Create your views here.
def reservation_view(request):
    time_id = request.GET.get('time')
    time_object = DoctorTime.objects.get(id=time_id)
    insurance_choices = Patient.InsuranceType.choices

    doctor = time_object.doctor_date.doctor

    context = {
        'doctor': doctor,
        'datetime__date': time_object.doctor_date.date,
        'datetime__time': time_object.time,
        'insurance_choices': insurance_choices,
        'time': time_id,
    }
    return render(request, 'reservation.html', context)
