from django.shortcuts import render, redirect
from doctors.models import Doctor
from patients.models import Patient
# from appointments.models import Appointment


# Create your views here.
def home_view(request):
    # doctors = Doctor.objects.all()
    # top_doctors = []
    # for doctor in doctors:
    #     num_appo = Appointment.objects.filter(doctor=doctor).count()
    #     top_doctors.append({
    #         "doctor": doctor,
    #         "num_appo": num_appo,
    #     })
    # top_3_doctors = sorted(top_doctors, key=lambda x: x['num_appo'], reverse=True)[:3]
    #
    # for doctor in doctors:
    #     for tdoctor in top_3_doctors:
    #         if  not doctor.medical_code == tdoctor.doctor.medical_code:
    #             doctor.delete()

    if request.method == 'POST':
        national_id = request.POST.get('id')

        try:
            patient = Patient.objects.get(national_id=national_id)
            return redirect('tracking_view', patient.national_id)
        except Patient.DoesNotExist:
            top_doctors = Doctor.objects.order_by('?')[:3]
            newest_doctors = Doctor.objects.order_by('created_at')[:3]

            context = {
                'top_doctors': top_doctors,
                'newest_doctors': newest_doctors,
                'error': 'کد ملی وارد شده در سیستم ثبت نشده است.'
            }
            return render(request, 'home.html', context)

    top_doctors = Doctor.objects.order_by('?')[:3]
    newest_doctors = Doctor.objects.order_by('created_at')[:3]

    context = {
        'top_doctors': top_doctors,
        'newest_doctors': newest_doctors,
    }
    return render(request, 'home.html', context)
