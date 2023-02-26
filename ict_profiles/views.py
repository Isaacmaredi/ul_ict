from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, 
                                UpdateView, DeleteView)
from ict_accounts.models import Profile
from ict_licenses.models import License
from .forms import ProfileCreateForm
from .filters import ProfileFilter

# Create your views here.
class FilteredListView(ListView):
    
    class FilteredListView(ListView):
        filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, *args, **kwargs):
        context = super(FilteredListView,self).get_context_data(*args,**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        context['form'] = self.filterset.form
        context['total_users'] = self.filterset.qs.count()
        return context


class ProfileListView(LoginRequiredMixin, FilteredListView):
    model = Profile
    context_object_name = 'profiles'
    filterset_class = ProfileFilter

    paginate_by = 6

    template_name = 'ict_profiles/profile_list.html'    

class ProfileAdminListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profiles_admin'
    template_name = 'ict_profiles/profile_admin.html'
    paginate_by = 6


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'ict_profiles/profile_detail.html'

    
class ProfileAdminDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'ict_profiles/profile_admin_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.all()
        return context

class ProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = ProfileCreateForm
    model = Profile
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'ict_profiles/profile_update.html'

    def get_success_url(self):
        return reverse('ict_profiles:profile-admin-detail', kwargs={'pk': self.object.id})
    
    # def form_valid(self, form):
    #     form.instance.user_id = self.request.user.id
    #     return super().form_valid(form)
    
    # def test_func(self):
    #     profile = self.get_object()
    #     if self.request.user.id == profile.user_id:
    #         return True
    #     return False

class MyProfileView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    #login_url = '/accounts/login_view'
    context_object_name = 'my_profile'
    model = Profile
    template_name = 'ict_profile/my_profile.html'
    

    def get_object(self):
            try:
                self.profile = Profile.objects.get(pk=self.request.user.pk)
            except Profile.DoesNotExist:
                self.profile = None
            return self.profile
        
    def test_func(self):
        profile = self.get_object()
        if self.request.user.pk == profile.pk:
            print('User ID: ',self.request.user.pk, '-- Profile ID: ', profile.pk)
            return True
        return False
    
class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    pass

def license_notify(request):
    profiles = Profile.objects.all()
            
    # for profile in profiles:
    #     if profile.licenses:
    #         for license in profile.licenses.all():
    #             from_email = settings.EMAIL_HOST_USER
    #             to_email = license.owner.user.email
    #             subject = "Notification! Software License Renewal Due"
    #             if license.days_till_renewal <=180:         
    #                 if license.days_till_renewal > 90:
    #                     message = 'Alert! Due date for {} license renewal is in less than 6 months.  Renewal date is on {}'.format(license.name, license.next_renewal_date) 
    #                 elif license.days_till_renewal <= 90 and license.days_till_renewal > 0: 
    #                     message = 'Warning! Due date for {} license renewal is in less than 6 months.  Renewal date is on {}'.format(license.name, license.next_renewal_date) 
    #                 else:
    #                     message = 'Critical! The {} license renewal overdue.  The renewal date was on {}'.format(license.name, license.next_renewal_date) 
    #                 print(message) 
    #             send_mail(
    #                 subject,
    #                 message,
    #                 from_email,
    #                 [to_email],
    #                 fail_silently = True                      
    #              )             
                
            
    context = {
        'profiles':profiles,
       
    }
    
    return render(request, 'ict_profiles/notify.html',context)