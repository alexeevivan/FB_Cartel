from django import forms
from .models import User
from django.forms import fields
from captcha.fields import CaptchaField


class LoginForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь {username}» в системе не найден')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data
    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationUserForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    job_position = forms.CharField(required=False)
    email = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Введите номер телефона'
        self.fields['first_name'].label = 'Фамилия'
        self.fields['last_name'].label = 'Имя'
        self.fields['job_position'].label = 'Должность'
        self.fields['email'].label = 'E-mail'
    
    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['by', 'net', 'ru']:
            raise forms.ValidationError(f'Регистрация пользователя с таким e-mail невозможна')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Пользователь с таким e-mail уже зарегистрирован')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с «{username}» в качестве имени аккаунта уже существует')
        return username
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(f'Попробуйте сделать эту строчку идентичной верхней')
        return self.cleaned_data
    
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'confirm_password', 
            'first_name',
            'last_name', 
            'job_position', 
            'phone', 
            'email'
        ]

