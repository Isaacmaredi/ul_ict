from django_filters import FilterSet, DateFilter, NumberFilter, ChoiceFilter

from ict_accounts.models import Profile

class ProfileFilter(FilterSet):
    
    MONTH_CHOICES = [(x+1,x+1) for x in range(0,12)]
    print(MONTH_CHOICES)
    birth_date = ChoiceFilter(field_name='birth_date', lookup_expr='month', choices=MONTH_CHOICES, method='filter_by_month')

    class Meta:
        model = Profile
        fields = ['user']
    
    def filter_by_month(self, qs, name, value):
        return qs.filter(birth_date__month=value)
        
    def __init__(self, *args, **kwargs):
        super(ProfileFilter, self).__init__(*args, **kwargs)
        self.filters['user'].label = "Filter by User Name"
        self.filters['birth_date'].label = "Filter by Birth Date"