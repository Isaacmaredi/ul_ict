from django.template import Template, Context
from django.conf import settings
from django.core.mail import send_mail
# from templated_mail.mail import BaseEmailMessage
from django.contrib.auth import get_user_model
from django.shortcuts import render
from celery import shared_task
from ict_accounts.models import Profile
from ict_licenses.models import License


@shared_task
def license_renewal_notify():
    lic_users = License.objects.all()
    # for lic_user in lic_users:
    #     if lic_user.days_till_renewal <= 180 and lic_user.days_till_renewal >= 90:
    #         subject = 'Alert! License renewal due'
    #         message = 'Attention {}! Due date for {} license renewal is  in less than six months from now.  Exact renewal date is on {}'.format(lic_user.owner,lic_user.name, lic_user.next_renewal_date)
    #         recipient = lic_user.owner.user.email
    #         send_mail(
    #         subject,
    #         message,
    #         settings.EMAIL_HOST_USER,
    #         [recipient,'isaac.maredi@ul.ac.za'],
    #         fail_silently=True
    #         )
    #         print(lic_user.days_till_renewal)
        
    #     elif lic_user.days_till_renewal < 90 and lic_user.days_till_renewal > 0:
    #         subject = 'Warning! License renewal due'
    #         message = 'Warning {}! Due date for {} license renewal is  in less than three months from now.  Exact renewal date is on {}'.format(lic_user.owner,lic_user.name, lic_user.next_renewal_date)
    #         recipient = lic_user.owner.user.email
    #         print(lic_user.owner.user.email)
    #         send_mail(
    #         subject,
    #         message,
    #         settings.EMAIL_HOST_USER,
    #         [recipient,'isaac.maredi@ul.ac.za'],
    #         fail_silently=True
    #         )
    #     else:
    #         pass
            
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.licenses:
            for license in profile.licenses.all():
              
                from_email = settings.EMAIL_HOST_USER
                to_email = license.owner.user.email
                subject = "Notification! Software License Renewal Due"
                if license.days_till_renewal <=180:         
                    if license.days_till_renewal > 90:
                        message = 'Alert! Due date for {} license renewal is in less than 6 months.  Renewal date is on {}'.format(license.name, license.next_renewal_date) 
                    elif license.days_till_renewal <= 90 and license.days_till_renewal > 0: 
                        message = 'Warning! Due date for {} license renewal is in less than 6 months.  Renewal date is on {}'.format(license.name, license.next_renewal_date) 
                    else:
                        message = 'Critical! The {} license renewal overdue.  The renewal date was on {}'.format(license.name, license.next_renewal_date)         
                send_mail(
                    subject,
                    message,
                    from_email,
                    [to_email,'ikemaredi.developer@gmail.com'],
                    fail_silently = True                      
                    )             

                 
                
        
    