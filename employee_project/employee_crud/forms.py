from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =('fullname','mobile','emp_code','position')
        labels = { 
            'fullname':'Full Name',
            'emp_code': 'EMP.code'
        }

    def __init__(self,*arg,**kwargs):
        super(EmployeeForm,self).__init__(*arg,**kwargs)
        self.fields['position'].empty_label = "select"
        self.fields['emp_code'].required = False