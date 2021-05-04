from django import forms
from fickka.models import Profile
#from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm, PasswordChangeForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['type'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['type'] = 'password'


class EdithProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','date_joined', ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date_joined': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class EdithProfilePageForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['Biography','Gender','State','Occupation','Contact','fb_url', 'twitter_url', 'instagram_url','profile_pic', ]

        widgets = {
            'Biography': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Please start with http://'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control','placeholder':'Please start with http://'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Please start with http://'}),
            'Gender':forms.Select(attrs={'class': 'form-control'}),
            'Occupation': forms.Select(attrs={'class': 'form-control'}),
            'State': forms.TextInput(attrs={'class': 'form-control'}),
            'Contact': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateProfilePageForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['Biography','Gender','Contact','State','Occupation','Contact','fb_url', 'twitter_url', 'instagram_url','profile_pic', ]

        widgets = {
            'Biography': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Please start with http://'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control','placeholder':'Please start with http://'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Please start with http://'}),
            'Gender':forms.Select(attrs={'class': 'form-control'}),
            'Occupation': forms.Select(attrs={'class': 'form-control'}),
            'State': forms.TextInput(attrs={'class': 'form-control'}),
            'Contact': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PasswordChangeForms(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


