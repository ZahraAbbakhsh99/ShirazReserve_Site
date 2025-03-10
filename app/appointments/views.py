from django.shortcuts import render, redirect
from patients.models import Patient
from .models import Appointment
from times.models import DoctorTime, DoctorDate
from django.core.exceptions import *


# Create your views here.
def report_view(request, time_id):
    time_object = DoctorTime.objects.get(id=time_id)
    doctor = time_object.doctor_date.doctor

    if request.method == "POST":
        request.POST.error = None
        name = request.POST.get('name').split()
        firstname = name[0]
        lastname = name[1]
        national_id = request.POST.get('id')
        insurance_type = request.POST.get('insurance_type')
        gender = request.POST.get('gender')
        if gender == "خانم":
            gender = "زن"
        else:
            gender = "مرد"

        phone_number = request.POST.get('phone')

        try:
            is_exist = Patient.objects.filter(national_id=national_id)
            if not is_exist:
                patient = Patient(national_id=national_id, first_name=firstname, last_name=lastname, insurance_type=insurance_type, gender=gender,
                                  phone_number=phone_number)
                patient.full_clean()
                patient.save()
            else:
                patient = Patient.objects.get(national_id=national_id)
                patient.first_name = firstname
                patient.last_name = lastname
                patient.insurance_type = insurance_type
                patient.gender = gender
                if len(phone_number)==11:
                    patient.phone_number = phone_number
                else:
                    raise ValidationError("شماره همراه باید 11-رقم باشد.")
                patient.save()

        except ValidationError as e:
            insurance_choices = Patient.InsuranceType.choices
            time_object = DoctorTime.objects.get(id=time_id)
            doctor = time_object.doctor_date.doctor
            e_num = len(e.messages)
            context = {
                'doctor': doctor,
                'datetime__date': time_object.doctor_date.date,
                'datetime__time': time_object.time,
                'insurance_choices': insurance_choices,
                'time': time_id,
                'error': e.messages[e_num-1]
            }
            return render(request, 'reservation.html', context)

        appointment = Appointment.objects.create(doctor=doctor, patient=patient, time=time_object)
        time_object.available = False
        time_object.save()

    context = {
        'patient_name': appointment.patient.__str__(),
        'doctor_name': appointment.doctor.__str__(),
        'date': appointment.time.doctor_date.jalali_date,
        'time': appointment.time.jalali_time,
        'clinc_address': appointment.doctor.clinic_addresses,
        'appointment_code': appointment.id,
    }
    return render(request, 'report.html', context)


def tracking_view(request, national_id):
    appointments = Appointment.objects.filter(patient__national_id=national_id)
    patient = Patient.objects.get(national_id=national_id)
    count = appointments.count()
    if count == 0:
        isempty = True
    else:
        isempty = False

    context = {
        'appointments': appointments,
        'patient': patient,
        'isempty': isempty,
    }
    return render(request, 'appointment_history.html', context)
