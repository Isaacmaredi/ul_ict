import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import License

from django.utils.timezone import now
import datetime

class LicenseFilter(django_filters.FilterSet):
    
    STATUS_CHOICES =[
        ('More than 6 Months','More than 6 Months'),
        ('3 - 6 Months','3 - 6 Months'),
        ('Less than 3 Months','Less than  3 Months'),
        ('Expired','Expired'),
        ('Perpertual','Perpertual'),
        ] 

    status = django_filters.ChoiceFilter(label='Filter by Time to Expiry', method='filter_status', choices=STATUS_CHOICES)

    class Meta:
        model = License

        fields = ('name', 'software_category','owner')
        
    def filter_status(self, queryset, name, value):
        if value == 'More than 6 Months':
            expression = queryset.filter(next_renewal_date__gte=now() + datetime.timedelta(days=180))
        
        elif value == '3 - 6 Months':
            expression = queryset.filter(next_renewal_date__range=(now() + datetime.timedelta(days=90), now() + datetime.timedelta(days=180)))
        
        elif value == 'Less than 3 Months':
            expression = queryset.filter(next_renewal_date__range=(now() + datetime.timedelta(days=1), now() + datetime.timedelta(days=90)))
            
        elif value == 'Expired':
            expression = queryset.filter(next_renewal_date__lt=now() + datetime.timedelta(days=0))
            
        elif value == 'Perpertual':
            expression = queryset.filter(next_renewal_date__isnull=True)
        
        return expression
        
    def __init__(self, *args, **kwargs):
        super(LicenseFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label="Type License Name"
        self.filters['owner'].label="Select License Owner"
        self.filters['software_category'].label="Filter by Software Category"
        self.filters['name'].lookup_expr = 'icontains'
        self.filters['name'].auto_complete = True
        
