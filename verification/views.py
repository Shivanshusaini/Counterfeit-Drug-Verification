from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import DrugBatch
from django.db import OperationalError  # Add this line
from django.http import HttpResponse
import os
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
# Create a superuser programmatically for render.com deployment



def create_admin(request):
    # Check if admin already exists
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse("❌ Admin already exists. Route disabled.")

    # Create admin
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="Admin@123"
    )

    # Auto-disable: comment out the route itself in urls.py
    project_urls = os.path.join(os.path.dirname(os.path.dirname(__file__)), "mysite", "urls.py")

    try:
        with open(project_urls, "r") as f:
            content = f.read()

        safe_content = content.replace(
            'path("create-admin/", create_admin),',
            '# path("create-admin/", create_admin),   # Auto-disabled'
        )

        with open(project_urls, "w") as f:
            f.write(safe_content)

    except Exception as e:
        return HttpResponse(f"Admin created, but failed to auto-disable: {e}")

    return HttpResponse("✅ Admin created and route auto-disabled!")