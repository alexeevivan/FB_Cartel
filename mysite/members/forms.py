from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models.fields import related
from django.forms import widgets, ModelForm

from captcha.fields import CaptchaField

from mainapp.models import *

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'Логин'
        self.fields['email'].label = 'E-mail'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'


    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['by', 'net', 'ru']:
            raise forms.ValidationError(f'Регистрация пользователя с таким e-mail невозможна')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Пользователь с указанным выше e-mail уже зарегистрирован')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if username in ['лох', 'ЛОХ', 'лОх', 'лОХ', 'ЛоХ', 'л0х', 'Л0х', 'л0Х', 'Л0Х']:
            raise forms.ValidationError(f'Регистрация пользователя с таким именем невозможна!')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Имя Пользователя «{username}» зарезервировано')
        return username

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'password')


class ProfilePageForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ('bio', 'workplace','profile_img', 'instagram_url', 'vk_url', 'facebook_url', 'twitter_url')
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Введите краткую информацию о себе'}),
            #'profile_img': forms.ImageField(choices=choice_list, attrs={'class':'form-control-select'}),
            'workplace' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Вы можете указать место работы'}),
            'instagram_url' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Вы можете указать ссылку на Ваш профиль в Instagram'}),
            'vk_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Вы можете указать ссылку на Ваш профиль в VK'}),
            'facebook_url' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Вы можете указать ссылку на Ваш профиль в Facebook'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Вы можете указать ссылку на Ваш профиль в Twitter'})
        }
    

class ProfileEditForm(UserChangeForm):
    # названия всех ниже перечисленных полей взято после того, как была проинспектирована страница
    # редактирования профиля (и после id у каждой строки были взяты названия)
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check', 'type':'hidden'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check', 'type':'hidden'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check', 'type':'hidden'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))


    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'E-mail'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['username'].label = 'Имя пользователя'
        self.fields['last_login'].label = 'Дата последнего входа в аккаунт'
        self.fields['date_joined'].label = 'Дата регистрации'
        

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')


class PasswordChangingForm(PasswordChangeForm):
    
    old_password = forms.EmailField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))


    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')