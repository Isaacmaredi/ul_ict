from re import S
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models.aggregates import Sum
from django.db.models import Value, DecimalField
from django.db.models.functions import Coalesce
from django.urls import reverse, reverse_lazy
from datetime import datetime, date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView,
                                CreateView,UpdateView,
                                DeleteView)
from .models import Contract
from .filters import ContractFilter
from .forms import ContractCreateForm
# from .filters import ContractFilter
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
        context['total_contracts'] = self.filterset.qs.count()
        return context
    
class ContractListView(LoginRequiredMixin ,FilteredListView):
    model = Contract
    template_name = 'ict_contracts/contract_list.html'
    filterset_class = ContractFilter
    context_object_name = 'contracts'
    paginate_by = 6
    
    def get_context_data(self, *args, **kwargs):
        context= super(ContractListView, self).get_context_data(*args, **kwargs)
        return context
    
class ContractAdminListView(LoginRequiredMixin, FilteredListView):
    model = Contract
    context_object_name = 'contracts'
    filterset_class = ContractFilter
    template_name = 'ict_contracts/contract_admin.html'
    paginate_by = 8
    
    # def get_context_data(self, queryset=None, *args, **kwargs):
    #     context= super(ContractAdminListView, self).get_context_data(*args,**kwargs)
    #     return context
        
        # status_ok_count = len([obj for obj in Contract.objects.all() if obj.status == "Ok"]) 
        # status_warning1_count = len([obj for obj in Contract.objects.all() if obj.status == "Attention"])
        # status_warning2_count = len([obj for obj in Contract.objects.all() if obj.status == "Warning"])
        # status_perpertual_count = len([obj for obj in Contract.objects.all() if obj.status == "Perpertual"])
        # status_expired_count = len([obj for obj in Contract.objects.all() if obj.status == "Expired"])
        
        # context['status_ok_count'] = status_ok_count
        # context['status_warning1_count'] = status_warning1_count
        # context['status_warning2_count'] = status_warning2_count
        # context['status_perpertual_count'] = status_perpertual_count
        # context['status_expired_count'] = status_expired_count
        # context['total_contracts_count'] = Contract.objects.all().count()
        # context['form'] = self.filterset.form

        # return context

class ContractDetailView(LoginRequiredMixin,DetailView):
    model = Contract
    template_name = 'ict_contracts/contract_detail.html'
    context_object_name = 'contract'  
    
    def get_context_data(self, queryset= None, *args, **kwargs):
        
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
    
        if pk is not None:
            queryset = queryset.filter(pk=pk)
            object = queryset[0]
            print(object.status)
            today = date.today()
            # print(today)
            # print('END DATE IS',object.end_date)
        
            if not self.object.end_date:
                days_until= -9999
                # print('DAYS TO:', days_until)
                # print(type(days_until))
            else:
                days = self.object.end_date - today
                days_until= int(str(days).split(' ')[0]) 
                # days_until = int(days_until, *args)
                # print('DAYS TO:',days_until)
                # print(type(days_until))
            print('-'*25)
    
        # print('PRIMARY KEY IS: ',self.object.pk)
        # print('DAYS UNTIL: ', days_until)
    
        
        if days_until > 365:  
            self.status = "Ok"
        elif days_until < 365 and days_until >= 180:
            self.status = "Attention"
        elif days_until < 180 and days_until >= 0:
            self.status = "Warning"
        elif days_until == -9999:
            self.status = "Perpertual"
        else:
            self.status = "Expired"
        
        context = super(ContractDetailView, self).get_context_data(*args, **kwargs)
        context['days_until'] = days_until
        context['amount_outstanding'] = self.object.total_value -  queryset.aggregate(
                        amount_outstanding= Coalesce(
                            Sum('licenses__current_cost' 
                            ,output_field=DecimalField()), 
                            Value(0,output_field=DecimalField())
                        )
                    )['amount_outstanding']
        return context 


class ContractAdminDetailView(LoginRequiredMixin,DetailView):
    model = Contract
    template_name = 'ict_contracts/contract_admin_detail.html'
    context_object_name = 'contract'    


class ContractCreateView(LoginRequiredMixin, CreateView):
    form_class = ContractCreateForm
    model = Contract 
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
# class ContractCreateView(LoginRequiredMixin, CreateView):
#     form_class = ContractCreateForm
#     model = Contract 
    
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)

class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractCreateForm
    template_name = 'ict_contracts/contract_update.html'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class ContractDeleteView(LoginRequiredMixin,DeleteView):
    model = Contract
    template_name = 'ict_contracts/contract_confirm_delete.html'
    success_url = reverse_lazy('ict_contracts:contract-admin')
    
