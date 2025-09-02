from django.urls import path
from . import views


urlpatterns=[
path('',views.home, name='home'),
path('about/',views.about,name='about'),
path('contact/',views.contact, name='contact'),
path('verify/batch/<str:serial_number>/', views.verify_batch, name='verify_batch'), # update
]