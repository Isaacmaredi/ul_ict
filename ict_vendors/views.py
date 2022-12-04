from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,ListView,
                                DetailView,UpdateView,DeleteView)
from .forms import VendorCreateForm

from .models import Vendor
# Create your views here.
class VendorListView(LoginRequiredMixin,ListView):
    model = Vendor
    template_name = 'ict_vendors/vendor_list.html'
    paginate_by = 15
    context_object_name = 'vendors'
    
    def get_context_data(self,*args,**kwargs):
        context = super(VendorListView, self).get_context_data(*args, **kwargs)
        context['total_vendors'] = Vendor.objects.all().count()
        # context['mncs'] = Vendor.objects.filter(location_type='MNC').count()
        return context

class VendorAdminListView(LoginRequiredMixin,ListView):
    model = Vendor
    template_name = 'ict_vendors/vendor_admin.html'
    paginate_by = 15
    context_object_name = 'vendors'
    
    def get_context_data(self,*args,**kwargs):
        context = super(VendorAdminListView, self).get_context_data(*args, **kwargs)
        context['total_vendors'] = Vendor.objects.all().count()
        return context

class VendorDetailView(LoginRequiredMixin,DetailView):
    model = Vendor
    context_object_name = 'vendor'

class VendorAdminDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'vendor'
    template_name = 'ict_vendors/vendor_admin_detail.html'
    
    
class VendorCreateView(LoginRequiredMixin,CreateView):
    form_class = VendorCreateForm
    model = Vendor

    
class VendorUpdateView(LoginRequiredMixin,UpdateView):
    model = Vendor
    form_class = VendorCreateForm
    template_name='ict_vendors/vendor_update.html'

class VendorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendor
    success_url = reverse_lazy('ict_vendors:vendor-admin')
    

    
    
