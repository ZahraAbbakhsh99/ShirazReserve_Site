from django.shortcuts import render, get_object_or_404
from .models import *
# from datetime import date
from times.models import DoctorDate, DoctorTime


# Create your views here.
def doctor_detail_view(request, medical_code):
    doctor = get_object_or_404(Doctor, medical_code=medical_code)
    processed_times = []
    dates = DoctorDate.objects.filter(doctor=doctor)

    for Ddate in dates:
        available_count = DoctorTime.objects.filter(doctor_date=Ddate, available=True).count()
        if available_count == 0:
            status = "تکمیل"
        else:
            status = f"{available_count} نوبت خالی "
        processed_times.append({
            "status": status,
            "date": Ddate,
            "hour": DoctorTime.objects.filter(doctor_date=Ddate),
            "jalali_date": Ddate.jalali_date,
        })

    context = {
        'doctor': doctor,
        # 'times': "date",
        'processed_times': processed_times,
    }
    return render(request, 'doctor_details.html', context)
