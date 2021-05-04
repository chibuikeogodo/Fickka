from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignupForm, EdithProfileForm, PasswordChangeForms, EdithProfilePageForm, CreateProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
#from .models import UserProfile
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView
from django.contrib import auth
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from fickka.models import Profile, Post
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def password_change(request):
    return render(request, 'password_success.html')


class Signup(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = 'register.html'

    def get_success_url(self):
        messages.success(self.request, 'Your account has being created successfully, Please login')
        return reverse('login')


def login(request):
    url = 'login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You're Logged in successfully")
            return redirect('home')
        else:
            messages.success(request, 'Sorry an error occurred,Please Try checking your details well')
            return redirect('login')
    return render(request, url)


def logout(request):
    auth.logout(request)
    return redirect('login')


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    form_class = EdithProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForms
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'use_profile.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user

        return context


class EdithProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'edith_profile_page.html'
    #fields = ['Biography', 'profile_pic', 'fb_url', 'twitter_url', 'instagram_url']
    form_class = EdithProfilePageForm
    success_url = reverse_lazy('home')


class CreateProfile(CreateView):
    model = Profile
    template_name = 'Create_profile.html'
    form_class = CreateProfilePageForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProfile, self).form_valid(form)

