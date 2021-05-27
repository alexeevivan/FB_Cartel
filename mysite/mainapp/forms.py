from django import forms
from .models import User
from django.forms import fields
from captcha.fields import CaptchaField


class LoginForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login'
        self.fields['password'].label = 'Password'
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'There is no Esse account with the «{username}» username you provided')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Wrong password')
        return self.cleaned_data
    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationUserForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
        self.fields['confirm_password'].label = 'Confirm the password'
        self.fields['phone'].label = 'Phone number'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['address'].label = 'Location'
        self.fields['email'].label = 'E-mail'
    
    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['by', 'net', 'ru']:
            raise forms.ValidationError(f'Registration of a user with such an e-mail is not possible')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'There is an other user registered in thhe system with such an e-mail')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'User with «{username}» as a nickname already exixsts')
        return username
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(f'Passwords don''t match')
        return self.cleaned_data
    
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'confirm_password', 
            'first_name',
            'last_name', 
            'address', 
            'phone', 
            'email'
        ]

