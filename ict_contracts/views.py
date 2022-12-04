from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contract
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView,
                                CreateView,UpdateView,
                                DeleteView)

from .forms import ContractCreateForm
# from .filters import ContractFilter
# Create your views here.
class ContractListView(ListView):
    model = Contract
    template_name = 'ict_contracts/contract_list.html'
    context_object_name = 'contracts'
    paginate_by = 10
    
    def get_context_data(self, *args, **kwargs):
        context= super(ContractListView, self).get_context_data(*args, **kwargs)
        # context['filter'] = ContractFilter(self.request.GET, queryset=self.get_queryset())
        context['total_contracts'] = Contract.objects.all().count()
        return context

# def contract_list(request):
#     contracts = Contract.objects.all()
    

class ContractAdminListView(LoginRequiredMixin, ListView):
    model = Contract
    context_object_name = 'contracts'
    template_name = 'ict_contracts/contract_admin.html'
    paginate_by = 10
    
    
    def get_context_data(self, *args, **kwargs):
        context= super(ContractAdminListView, self).get_context_data(*args,**kwargs)
        context['total_contracts'] = Contract.objects.all().count()
        return context

class ContractDetailView(LoginRequiredMixin,DetailView):
    model = Contract
    template_name = 'ict_contracts/contract_detail.html'
    context_object_name = 'contract'   

class ContractAdminDetailView(LoginRequiredMixin,DetailView):
    model = Contract
    template_name = 'ict_contracts/contract_admin_detail.html'
    context_object_name = 'contract'    


class ContractCreateView(LoginRequiredMixin, CreateView):
    form_class = ContractCreateForm
    model = Contract
    
    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        return super().form_valid(form)
    
    
class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractCreateForm
    template_name = 'ict_contracts/contract_update.html'
    
    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        return super().form_valid(form)
    
    
class ContractDeleteView(LoginRequiredMixin,DeleteView):
    model = Contract
    template_name = 'ict_contracts/contract_confirm_delete.html'
    success_url = reverse_lazy('ict_contracts:contract-admin')
    
