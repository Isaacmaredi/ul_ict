from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (ProfileListView, ProfileDetailView,
                    ProfileCreateView, ProfileUpdateView,ProfileDeleteView,
                    ProfileAdminListView, ProfileAdminDetailView, MyProfileView
                    )

from django.contrib.auth.decorators import login_required

app_name = 'ict_profiles'

urlpatterns = [
    path('profile_list/', ProfileListView.as_view(), name = 'profile-list'),
    path('<int:pk>/profile_detail/', ProfileDetailView.as_view(), name ='profile-detail'),
    path('<int:pk>/my_profile/',login_required(MyProfileView.as_view(template_name='ict_profiles/my_profile.html')),name ='my-profile'),
    path('profile_admin/',ProfileAdminListView.as_view(), name = 'profile-admin'),
    path('<int:pk>/detail', ProfileAdminDetailView.as_view(), name='profile-admin-detail'),
    path('profile_add/', ProfileCreateView.as_view(), name='profile-add'),
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]