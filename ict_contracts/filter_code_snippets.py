# filters.py
from .models import Contract
import datetime

from django_filters import FilterSet
from django.utils.timezone import now

class ContractFilter(FilterSet):
    class Meta:
        model = Contract
        fields = ['name', 'supplier', 'contract_owner']
    
    def filter_status(self, queryset, name, value):
        if value == 'Ok':
            expression = queryset.filter(end_date__gte=now() + datetime.timedelta(days=360))
        elif value == 'Attention':
            expression = queryset.filter(end_date__range=(now() + datetime.timedelta(days=180), now() + datetime.timedelta(days=360)))
        elif value == 'Warning':
            expression = queryset.filter(end_date__lte=now() + datetime.timedelta(days=90))
        elif value == 'Expired':
            expression = queryset.filter(end_date__lte=now())
        elif value == 'Perpetual':
            expression = queryset.filter(end_date__isnull=True)
        return expression