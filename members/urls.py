from django.urls import path
from .views import Signup, login, logout, \
    UserEditView, PasswordChangeView, password_change, \
    ShowProfilePageView, EdithProfilePageView, CreateProfile
from django.contrib.auth import views as auth_views


urlpatterns = [

    ##Members
    path('register/', Signup.as_view() , name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('members/edit_profile', UserEditView.as_view(), name='edith_profile'),
    path('password/', PasswordChangeView.as_view(), name='change_password' ),
    path('password_change_success/', password_change, name='password_change'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='Show_Profile_PageView'),
    path('<int:pk>/edith_profile_page', EdithProfilePageView.as_view(), name='Edith_Profile_PageView'),
    path('Create_profile', CreateProfile.as_view(), name='Create_profile'),


]
