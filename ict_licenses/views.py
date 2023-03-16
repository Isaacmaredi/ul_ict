from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,
                                CreateView,UpdateView,DeleteView)

from .models import License, LicenseRenewal
from .forms import LicenseCreateForm, LicenseRenewalForm

from datetime import datetime, date, timedelta
from django.utils import timezone
from .filters import LicenseFilter

# Create your views here.

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
        context['total_licenses'] = self.filterset.qs.count()
        return context
    
class LicenseListView(LoginRequiredMixin ,FilteredListView):
    model = License
    template_name = 'ict_licenses/license_list.html'
    filterset_class = LicenseFilter
    context_object_name = 'licenses'
    paginate_by = 5
    
    def get_context_data(self, *args, **kwargs):
        context= super(LicenseListView, self).get_context_data(*args, **kwargs)
        return context

class LicenseAdminListView(LoginRequiredMixin, FilteredListView):
    model = License
    context_object_name = 'licenses'
    filterset_class = LicenseFilter
    template_name = 'ict_licenses/license_admin.html'
    paginate_by = 5
    
    def get_context_data(self, *args, **kwargs):
        context = super(LicenseAdminListView, self).get_context_data(*args, **kwargs)
        return context 

class LicenseDetailView(LoginRequiredMixin, DetailView):
    model = License
    context_object_name ='license'
    template_name ='ict_licenses/license_detail.html'
    
class LicenseAdminDetailView(LoginRequiredMixin, DetailView):
    model = License
    context_object_name = 'license'
    template_name ='ict_licenses/license_admin_detail.html'
    
    def get_context_data(self,*args, **kwargs):     
        context = super(LicenseAdminDetailView, self).get_context_data(*args,**kwargs)
        context['amount_outstanding'] = self.object.name
        return context
    
    
class LicenseCreateView(LoginRequiredMixin, CreateView):
    form_class = LicenseCreateForm
    model = License
    # template_name ='licenses/license-form-test.html'
    
    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)
    
class LicenseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = LicenseCreateForm
    model = License
    context_object_name = 'license'
    template_name ='ict_licenses/license_update.html'
       
    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)
    
    def test_func(self):
        license = self.get_object()  
        
        if self.request.user.id == license.owner_id:
            print('User ID: ',self.request.user.id, '-- Owner ID: ', license.owner_id)
            return True
        return False  

class LicenseRenewalView(LoginRequiredMixin,CreateView):
    form_class = LicenseRenewalForm
    model = LicenseRenewal
    context_object_name = 'license_renewal'
    template_name ='ict_licenses/license_renew.html'
    
    def form_valid(self, form):  
        form.instance.owner_id = self.request.user.id
        form.save()
        messages.add_message(
            self.request, messages.SUCCESS, f'{form.instance.name}license has been succesfully renewed! Renewal date starts on {form.instance.renewal_date}!')
        return super().form_valid(form)
        
    # def test_func(self, *args, **kwargs):
    #     self.license = self.get_object()
    #     if self.request.user.id == self.license.owner_id:
    #         # print('User ID: ',self.request.user.id, '-- Owner ID: ', license.owner_id)
    #         return True
        
    #     return False
        #     errors = messages.error(self.request,  f'You are not allowed to edit this {license.name} license')
        # return r
    
    
class LicenseDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = License
    success_url = reverse_lazy('ict_licenses:license-admin')
    
    def test_func(self, *args, **kwargs):
        self.license = self.get_object()
        if self.request.user.id == self.license.owner_id:
            # print('User ID: ',self.request.user.id, '-- Owner ID: ', license.owner_id)
            return True
        
        return False


