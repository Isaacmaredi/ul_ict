from time import sleep, strftime
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from ict_licenses.models import License
from ict_accounts.models import Profile

from django.utils.timezone import now
from datetime import datetime, date



def license_renewal_notify(request):
    # lic_users = License.objects.all()
    profiles = Profile.objects.all()

    for profile in profiles:
        licenses = profile.licenses.all()
        for license in licenses:
            if license.days_till_renewal <= 180 and license.days_till_renewal>=90:
                print('Attention ', license.owner, 'The license for ', license.name, 'expires on',license.next_renewal_date)
            elif license.days_till_renewal < 90 and license.days_till_renewal > 0:
                print('Warning ', license.owner, 'The license for ', license.name, 'expires on',license.next_renewal_date)
            else:
                pass  
    
    # for lic_user in lic_users:
        
        #   if lic_user.days_till_renewal <= 180 and lic_user.days_till_renewal >= 90:
        #     subject = 'Alert! License renewal due'
        #     message = 'Attention {}! Due date for {} license renewal is  in less than six months from now.  Exact renewal date is on {}'.format(lic_user.owner,lic_user.name, lic_user.next_renewal_date)
        #     recipient = lic_user.owner.user.email
        #     send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [recipient,'isaac.maredi@ul.ac.za'],
        #     fail_silently=True
        #     )
        #     print(lic_user.days_till_renewal)
            
        # elif lic_user.days_till_renewal < 90 and lic_user.days_till_renewal > 0:
        #     subject = 'Warning! License renewal due'
        #     message = 'Warning {}! Due date for {} license renewal is  in less than three months from now.  Exact renewal date is on {}'.format(lic_user.owner,lic_user.name, lic_user.next_renewal_date)
        #     recipient = lic_user.owner.user.email
        #     send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [recipient,'isaac.maredi@ul.ac.za'],
        #     fail_silently=True
        #     )
        #     print(lic_user.days_till_renewal)
            
        # else:
        #     pass
            
        context = {
            'profiles':profiles,
            }
    return render(request, 'ict_tasks/tasks.html', context)


