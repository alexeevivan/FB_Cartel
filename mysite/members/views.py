from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView
from .forms import *
from mainapp.models import *
# этот импорт сделан для того, чтобы работать с изменением пароля пользователя на странице
from django.contrib.auth.views import PasswordChangeView


class UserRegisterView(CreateView):
    
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileView(TemplateView):
     
    template_name = 'registration/profile.html'


class ProfileEditView(UpdateView):
     
    form_class = ProfileEditForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user


class ProfileShowPageView(DetailView):
     
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileShowPageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        context['page_user'] = page_user
        return context


class ProfileEditPageView(UpdateView):
     
    model = Profile
    template_name = 'registration/profile_edit_page.html'
    # поля из models.Profile
    fields = ['bio', 'profile_img', 'instagram_url', 'vk_url', 'facebook_url', 'twitter_url']
    success_url = reverse_lazy('index')


 
class PasswordEditView(PasswordChangeView):
     
    # раньше была стандартная форма PasswordChangeForm
    # но сейчас другая у form_class, так как была создана в файле forms.py
    # собственная форма, лишь основанная на PasswordChangeForm для того, чтобы
    # можно было прописать стили в CSS
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    template_name = 'password-edit.html'
    success_url = reverse_lazy('profile')