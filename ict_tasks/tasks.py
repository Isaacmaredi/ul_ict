from django.template import Template, Context
from django.conf import settings
from django.core.mail import send_mail
from templated_mail.mail import BaseEmailMessage
from django.contrib.auth import get_user_model
from django.shortcuts import render
from celery import shared_task
from ict_accounts.models import Profile
from ict_licenses.models import License


@shared_task
def license_renewal_notify():
    profiles = Profile.objects.all()
    lic_users = License.objects.all()
    msg_list = []

    days_left_list   = []
    
    for profile in profiles:
        if profile.licenses.all().count() > 0:
            count = profile.licenses.all().count()
            # print('@'*25)
            # print('No. of Licenses for', profile, ':',count )
            # print('@'*25)
            licenses = profile.licenses.all()       
            for license in licenses:
                if license.days_till_renewal <= 180:
                    msg = f'Warning!  - {license.name} license expires in less than 6 months. {license.next_renewal_date} - and you have {license.days_till_renewal} days left to renew!'  if license.days_till_renewal >90 else f'Critical! {license.name} license expires in less than 3 months. The expiry date is {license.next_renewal_date} - and you have {license.days_till_renewal} days left to renew!'
                    # print('OWNER: ',license.owner,'LICENSE: ', license.name)
                    days_left_list.append(license.days_till_renewal)
                    msg_list.append(msg)
                
                days_left_list = days_left_list
                msg_list = msg_list
                message_list = zip(msg_list, days_left_list)
                license_owner = license.owner
                to_email = license.owner.user.email
            BaseEmailMessage (
                        template_name = 'emails/license_notification.html',
                        context = {
                            'days_left_list':days_left_list,
                            'license_owner':license_owner,
                            'message_list':message_list,
                            },      
                            
                ).send(to=[to_email])
        for m in message_list:
            print(m)
        msg_list = []
        days_left_list = []
        message_list = []
        
    
            
   
                
        
    