from django import forms
from django.contrib.auth.models import User
from django.db import transaction 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name',
                                 max_length=100,)
    last_name = forms.CharField(label='Last Name',
                                max_length= 100)
    country_code = forms.CharField(label='Country Code',
                                   max_length=5)
    phone = forms.CharField(label='Phone Number',
                            max_length=15)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            return forms.ValidationError('Las contraseñas no son iguales')
        return cd['password2']
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('El número de teléfono debe contener solo dígitos.')
        if len(phone) < 7 or len(phone) > 15:
            raise forms.ValidationError('El número de teléfono debe tener entre 7 y 15 dígitos.')
        return phone
    
