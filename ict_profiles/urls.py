from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (ProfileListView, ProfileDetailView,
                    ProfileCreateView, ProfileUpdateView,ProfileDeleteView,
                    ProfileAdminListView, ProfileAdminDetailView, MyProfileView, license_notify
                    )

from django.contrib.auth.decorators import login_required

app_name = 'ict_profiles'

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name = 'profile-list'),
    path('profile_detail/<int:pk>/', ProfileDetailView.as_view(), name ='profile-detail'),
    path('my_profile/<int:pk>/',login_required(MyProfileView.as_view(template_name='ict_profiles/my_profile.html')),name ='my-profile'),
    path('profile_admin/',ProfileAdminListView.as_view(), name = 'profile-admin'),
    path('profile_detail/<int:pk>/', ProfileAdminDetailView.as_view(), name='profile-admin-detail'),
    path('profile_add/', ProfileCreateView.as_view(), name='profile-add'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile_delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('license_notify/', license_notify, name='license-notify')
]