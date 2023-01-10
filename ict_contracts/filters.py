from ast import expr_context
from tkinter import Y
from django import forms
from django.db import models
from django.db.models import Q
from datetime import date, timedelta
from django.forms import ModelForm

from django.http import QueryDict
import django_filters
from django_filters import DateFilter, CharFilter

from ict_contracts.forms import DateInput
from .models import Contract

class ContractFilter(django_filters.FilterSet):
    
   

    
    YEAR_CHOICES = ([(x+1, x+1) for x in range (1990, 2030)])


    
    end_date_year = django_filters.ChoiceFilter(field_name='end_date', choices=YEAR_CHOICES, label='Expiry Year', lookup_expr='year__exact')
    
    class Meta:
        model = Contract
        fields = ['name','supplier','owner']
    
    def __init__(self,*args, **kwargs):
        super(ContractFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label="Type contract name to search"
        self.filters['supplier'].label = "Select supplier to filter by"
        self.filters['owner'].label = "Select manager to filter by"
        self.filters['name'].lookup_expr = 'icontains'
        self.filters['supplier'].auto_complete = True
    
    
    