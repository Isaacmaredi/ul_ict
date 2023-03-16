from time import sleep, strftime
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from ict_licenses.models import License
from ict_accounts.models import Profile
from templated_mail.mail import BaseEmailMessage

from django.utils.timezone import now
from datetime import datetime, date

  

def license_renewal_notify(request):
    # lic_users = License.objects.all()
    profiles = Profile.objects.all()
    lic_users = License.objects.all()
    msg_list = []

    days_left_list   = []
    
    for profile in profiles:
        if profile.licenses.all().count() > 0:
            licenses = profile.licenses.all()       
            for license in licenses:
                if license.days_till_renewal <= 180:
                    msg = f'Warning!  - {license.name} license expires in less than 6 months. {license.next_renewal_date} - and you have {license.days_till_renewal} days left to renew!'  if license.days_till_renewal >90 else f'Critical! {license.name} license expires in less than 3 months. The expiry date is {license.next_renewal_date} - and you have {license.days_till_renewal} days left to renew!'
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
        owner = license.owner
      
    names = ['Isaac','Thabo','Tebogo','Tshililo']    
    
    context = {
    'name':'Licenses will come here',
    'names':names,
    'profiles':profiles,
    'owner':owner,
        }
    return render(request, 'ict_tasks/tasks.html', context)


