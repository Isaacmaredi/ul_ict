from django import forms
from django.db import models
from django.db.models import Q
import datetime 
from django.utils.timezone import now

import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter

from ict_contracts.forms import DateInput
from .models import Contract

class ContractFilter(django_filters.FilterSet):
    
    
    # YEAR_CHOICES = ([(x+1, x+1) for x in range (1990, 2030)])
    STATUS_CHOICES =[
        ('1 Year or More','1 Year or More'),
        ('6 - 12 Months','6 - 12 Months'),
        ('Less than 6 Months','Less than 6 Months'),
        ('Expired','Expired'),
        ('Perpertual','Perpertual'),
        ] 

    status = django_filters.ChoiceFilter(label='Filter by Time to Expiry', method='filter_status', choices=STATUS_CHOICES)
    
    class Meta:
        model = Contract
        fields = ['name','supplier','owner']
    
    def filter_status(self, queryset, name, value):
        if value == '1 Year or More':
            expression = queryset.filter(end_date__gte=now() + datetime.timedelta(days=360))
        
        elif value == '6 - 12 Months':
            expression = queryset.filter(end_date__range=(now() + datetime.timedelta(days=180), now() + datetime.timedelta(days=360)))
        
        elif value == 'Less than 6 Months':
            expression = queryset.filter(end_date__range=(now() + datetime.timedelta(days=1), now() + datetime.timedelta(days=180)))
            
        elif value == 'Expired':
            expression = queryset.filter(end_date__lt=now() + datetime.timedelta(days=0))
            
        elif value == 'Perpertual':
            expression = queryset.filter(end_date__isnull=True)
        
        return expression
    
    def __init__(self,*args, **kwargs):
        super(ContractFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label="Type Contract Name to Search"
        self.filters['supplier'].label = "Select Supplier to Filter by"
        self.filters['owner'].label = "Select Manager to Filter by"
        self.filters['name'].lookup_expr = 'icontains'
        self.filters['supplier'].auto_complete = True
    
    
    