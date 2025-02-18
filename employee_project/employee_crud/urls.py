from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.employee_form, name='employee_form'),  # Handle the root URL for this app
    path('list/', views.employee_list, name='employee_list'),
]
