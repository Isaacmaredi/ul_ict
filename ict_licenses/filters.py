import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import License

class LicenseFilter(django_filters.FilterSet):

    class Meta:
        model = License

        fields = ('name', 'software_category','owner')
        
    def __init__(self, *args, **kwargs):
        super(LicenseFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label="Type license name to search"
        self.filters['owner'].label="Select license owner to search"
        self.filters['software_category'].label="Filter by software category"
