from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,ListView,
                                DetailView,UpdateView,DeleteView)
from .forms import VendorCreateForm

from .models import Vendor
from .filters import VendorFilter
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
        context['total_vendors'] = self.filterset.qs.count()
        return context

class VendorListView(LoginRequiredMixin, FilteredListView):
    model = Vendor
    template_name = 'ict_vendors/vendor_list.html'
    paginate_by = 10
    filterset_class = VendorFilter
    context_object_name = 'vendors'

class VendorAdminListView(LoginRequiredMixin, FilteredListView):
    model = Vendor
    template_name = 'ict_vendors/vendor_admin.html'
    filterset_class = VendorFilter
    paginate_by = 10
    context_object_name = 'vendors'
    

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
    

    
    
