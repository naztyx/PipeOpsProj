from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import MedRecordForm


# Create your views here.
def signin_signup(request):
    return render(request, 'login_signup.html')

def home_dashboard(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'patient'):
            patient = request.user.patient
            medical_records = MedicalRecord.objects.filter(patient=patient)
            device_data = DeviceData.objects.filter(patient=patient)
            return render(request, 'home_dashboard.html', {
                'medical_records': medical_records,
                'device_data': device_data,
            })
        elif hasattr(request.user, 'doctor'):
            doctor = request.user.doctor
            schedules = Schedule.objects.filter(doctor=doctor)
            return render(request, 'physician_dashboard.html', {
                'schedules': schedules,
            })
    
    return render(request, 'home_dashboard.html')

def update_medical_record(request):
    if request.method == 'POST' and request.user.is_authenticated and hasattr(request.user, 'patient'):
        patient =request.user.patient
        form = MedRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = patient
            record.save()
            # record = request.POST.get('data')
            # MedicalRecord.objects.create(patient=patient, data=record)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})

def schedule_consultation(request):
    if request.method == 'POST' and request.user.is_authenticated and hasattr(requset.user, 'doctor'):
        doctor = request.user.doctor
        appointment_id = request.POST.get('appointment_id')
        virtual_consultation_link = request.POST.get('virtual_consultation_link')
        appointment = get_object_or_404(Schedule, id=appointment_id, doctor=doctor)
        Consultation.objects.create(appointment=appointment, virtual_consultation_link=virtual_consultation_link)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})
