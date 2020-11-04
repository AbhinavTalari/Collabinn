from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Company
from django.contrib.auth import authenticate, login

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Enter Valid Email ! Required Field')
    class Meta:
        model = Company
        fields = ('company_name','location','email', 'company_uid','date_of_est','expertise','interests','password1', 'password2',)

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Company
        fields = ('email', 'password')
        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")