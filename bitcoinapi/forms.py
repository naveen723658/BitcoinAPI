from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class signin(UserCreationForm):
    password1 = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {'email':'Email'}
        widgets ={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }


