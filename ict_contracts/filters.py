import django_filters
from django_filters import DateFilter, CharFilter
from .models import Contract

class ContractFilter(django_filters.FilterSet):
    description = CharFilter(field_name = "description", lookup_expr='icontains', label='Description')
    status = CharFilter(field_name = "status", lookup_expr='icontains', label="Status")
    class Meta:
        model = Contract
        fields = ('owner',)
                    
                    