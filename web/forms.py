from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'username']


        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class MyfileForm(ModelForm):
    class Meta:
        model = Myfile
        fields = '__all__'
        
class GovernanceForm(ModelForm):
    class Meta:
        model = Governance
        fields = '__all__'