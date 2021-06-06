from django import forms
from django.forms import ModelForm
from .models import *


class Inform(ModelForm):
    class Meta:
        model = Information
        fields = ('first_name', 'last_name', 'Email', 'LinkedIn', 'contact', 'address', 'exp')
        labels = {'first_name': '', 'last_name': '', 'Email': '', 'LinkedIn': ''}
        widgets = {'first_name':forms.TextInput(attrs={'class': 'form-control', "placeholder": 'First Name'}),
                  'last_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                  'Email':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'abc@defgh.ijk'}),
                  'LinkedIn':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ln/abcdef'})}


class EduForm(ModelForm):
    class Meta:
        model = Education
        fields = ('course_name', 'institute', 'score', 'pass_yr')
        labels = {'course_name': ''}
        widgets = {'course_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": 'Course'}),}


class ExpForm(ModelForm):
    class Meta:
        model = Experience
        fields = ('job', 'company', 'start_yr', 'designation', 'project', 'add')


class OrgForm(ModelForm):
    class Meta:
        model = Organization
        fields = ('name', 'type')
        labels = {'name': '', 'type': ''}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": 'Name'}),
                   'type': forms.TextInput(attrs={'class': 'form-control', "placeholder": 'Type'}) }

class ContForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('cont1', 'cont2')


class AddrsForm(ModelForm):
    class Meta:
        model = Addresse
        fields = ('Address1', 'Address2')