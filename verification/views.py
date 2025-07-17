from django.shortcuts import render,get_object_or_404
from .models import DrugBatch
from django.db import OperationalError  # Add this line
from django.http import HttpResponse
def home(request):
    result = None
    serial = request.GET.get('serial') or request.POST.get('serial_number')

    if serial:
        try:
            batch = DrugBatch.objects.get(serial_number=serial)
            result = f" ✅ Genuine | Drug: {batch.drug_name}, Batch: {batch.batch_number}"
        except DrugBatch.DoesNotExist:
            result = "❌ Counterfeit or Invalid Serial Number"
        except OperationalError:
            result = "⚠️ Database connection failed."

    return render(request, 'home.html', {'result': result})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
# Create your views here.

##################
def verify_batch(request, serial_number):
    batch = DrugBatch.objects.filter(serial_number=serial_number).first()
    if batch:
        return render(request, 'verify_result.html', {'batch': batch})
    return HttpResponse("❌ No batch found! Counterfeit or Invalid Serial Number.")
#################