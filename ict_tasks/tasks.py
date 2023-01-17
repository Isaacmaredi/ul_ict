# from django.template import Template, Context
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.shortcuts import render
from celery import shared_task
from ict_licenses.models import License


@shared_task
def license_renewal_notify():
    lic_users = License.objects.all()
    for lic_user in lic_users:
        if lic_user.days_till_renewal <= 180 and lic_user.days_till_renewal >= 90:
            subject = 'Alert! License renewal due'
            message = 'Attention {}! Due date for {} license renewal is  in less than six months from now.  Exact renewal date is on {}'.format(lic_user.owner,lic_user.name, lic_user.next_renewal_date)
            recipient = lic_user.owner.user.email
            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient,'isaac.maredi@ul.ac.za'],
            fail_silently=True
            )
            print(lic_user.days_till_renewal)
        
        elif lic_user.days_till_renewal < 90 and lic_user.days_till_renewal > 0:
            subject = 'Warning! License renewal due'
            message = 'Warning {}! Due date for {} license renewal is  in less than three months from now.  Exact renewal date is on {}'.format(lic_user.owner,lic_user.name, lic_user.next_renewal_date)
            recipient = lic_user.owner.user.email
            print(lic_user.owner.user.email)
            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient,'isaac.maredi@ul.ac.za'],
            fail_silently=True
            )
        else:
            pass
            
    