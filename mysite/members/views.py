from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import *
# этот импорт сделан для того, чтобы работать с изменением пароля пользователя на странице
from django.contrib.auth.views import PasswordChangeView


class PasswordEditView(PasswordChangeView):
     
     # раньше была стандартная форма PasswordChangeForm
     # но сейчас другая у form_class, так как была создана в файле forms.py
     # собственная форма, лишь основанная на PasswordChangeForm для того, чтобы
     # можно было прописать стили в CSS
     form_class = PasswordChangingForm
     #form_class = PasswordChangeForm
     template_name = 'password-edit.html'
     success_url = reverse_lazy('profile')


class UserRegisterView(CreateView):
    
     form_class = SignUpForm
     template_name = 'registration/register.html'
     success_url = reverse_lazy('login')


class ProfileView(TemplateView):
     
     template_name = 'profile.html'


class ProfileEditView(UpdateView):
     
     form_class = ProfileEditForm
     template_name = 'profile_edit.html'
     success_url = reverse_lazy('profile')
     
     def get_object(self):
          return self.request.user