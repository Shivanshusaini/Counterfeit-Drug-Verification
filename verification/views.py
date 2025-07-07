from django.shortcuts import render
from .models import DrugBatch
from django.db import OperationalError  # Add this line

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
