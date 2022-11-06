from django.urls import path
from . import views

app_name = 'ict_accounts'

urlpatterns = [
    path('register/', views.register, name = 'register'), 
    path('', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password_change/', views.MyPasswordChangeView.as_view(), name = 'password-change'),
    path('password_change_done/', views.MyPasswordChangeDoneView.as_view(), name = 'password-change-done'),
    path('forgot_password/', views.forgot_password, name='forgot-password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset-password-validate'),
    path('reset_password/', views.reset_password, name='reset-password'),
]