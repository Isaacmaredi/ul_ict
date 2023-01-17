from django.urls import path
from .views import license_renewal_notify

app_name = 'ict_tasks'

urlpatterns = [
    path('email_notify/', license_renewal_notify, name='email-notify')
]
