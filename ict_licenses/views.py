from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,
                                CreateView,UpdateView,DeleteView)

from .models import License
from .forms import LicenseCreateForm

from datetime import datetime, date, timedelta
from django.utils import timezone

# Create your views here.

class LicenseListView(LoginRequiredMixin, ListView):
    model = License  
    context_object_name ='licenses'
    template_name ='ict_licenses/license_list.html'
    paginate_by = 10
    
    def get_context_data(self,*args, **kwargs):
        context = super(LicenseListView, self).get_context_data(*args,**kwargs)
        context['tot_licenses'] = License.objects.all().count()
        return context

class LicenseAdminListView(LoginRequiredMixin, ListView):
    model = License
    context_object_name = 'licenses'
    template_name = 'ict_licenses/license_admin.html'
    paginate_by = 10
    
    def get_context_data(self, *args, **kwargs):
        context = super(LicenseAdminListView, self).get_context_data(*args, **kwargs)
        context['tot_licenses'] = License.objects.all().count()
        return context 

class LicenseDetailView(LoginRequiredMixin, DetailView):
    model = License
    context_object_name ='license'
    template_name ='ict_licenses/license_detail.html'
    
class LicenseAdminDetailView(LoginRequiredMixin, DetailView):
    model = License
    context_object_name = 'license'
    template_name ='ict_licenses/license_admin_detail.html'
    
    
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
    
class LicenseDeleteView(LoginRequiredMixin, DeleteView):
    model = License
    success_url = reverse_lazy('ict_licenses:license-admin')


