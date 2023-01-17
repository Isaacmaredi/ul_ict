from django_filters import FilterSet, DateFilter, NumberFilter, ChoiceFilter

from ict_accounts.models import Profile

class ProfileFilter(FilterSet):
    
    MONTH_CHOICES = [
        ('1','January'),
        ('2','February'),
        ('3','March'),
        ('4','April'),
        ('5','May'),
        ('6','June'),
        ('7','July'),
        ('8','August'),
        ('9','September'),
        ('10','October'),
        ('11','November'),
        ('12','December'),
    ]
    
    birth_date = ChoiceFilter(field_name='birth_date', lookup_expr='month', choices=MONTH_CHOICES, method='filter_by_month')

    class Meta:
        model = Profile
        fields = ['user']
    
    def filter_by_month(self, qs, name, value):
        return qs.filter(birth_date__month=value)
        
    def __init__(self, *args, **kwargs):
        super(ProfileFilter, self).__init__(*args, **kwargs)
        self.filters['user'].label = "Filter by User Name"
        self.filters['birth_date'].label = "Filter by Birth Month"