from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView

# User activation
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from django.contrib.auth.views import PasswordResetView

from .models  import Account, Profile
from .forms import RegistrationForm, MyPasswordResetForm

from django.template import RequestContext

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.mobile_number = mobile_number
            user.save()
            
            #Notfify Admin about new signup 
            send_mail('New user registration alert',
                    f'{first_name} {last_name} has been registered as a new user and is pending verification',
                    email,
                    ['isaac.maredi@gmail.com'],
                    fail_silently=False)
            
            #Account Verification
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('ict_accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email,'ikemaredi.developer@gmail.com'])
            send_email.send()
            messages.success(request, f'Thank you for registering. A verification email has been sent to your email address {to_email}. Please check and verify it.')
            return redirect('/?command=verification&email='+email)
            
        
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'ict_accounts/register.html', context)

#Account Activation
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated. You may now login')
        return redirect('ict_accounts:login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('ict_accounts:register')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password= request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            print(user, 'USER IS LOGGED IN ')
            messages.success(request, f'Welcome, {user.first_name}. Please find some time to update your profile if not done yet!')
            return redirect('ict_dash:dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('ict_accounts:login')
    else:
        return render(request, 'ict_accounts/login.html')

def logout_view(request): 
    auth.logout(request)
    return redirect ('ict_accounts:login')
        
    
class MyPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    template_name = 'ict_accounts/password_change_form.html'
    success_url = reverse_lazy ('ict_accounts:password-change-done')  
    success_message = 'Password changed successfully. You may login with your new password!'


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'ict_accounts/password_change_done.html'
    

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('ict_accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('ict_accounts:login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('ict_accounts:forgot-password')
    return render(request, 'ict_accounts/forgot_password.html')


def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('ict_accounts:reset-password')
    else:
        messages.error(request, 'This link has expired. Please run forgot password again!')
        return redirect('ict_accounts:login')
    

def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('ict_accounts:login')
        elif len(password)<8:
            print(len(password))
            messages.error(request,'Password is too short! Must be 8 characters or more.')
            return render(request, 'ict_accounts/reset_password.html')
        else:
            messages.error(request, 'Passwords did not match!')
            return redirect('ict_accounts:reset-password')
    else:
        return render(request, 'ict_accounts/reset_password.html')
