from django_filters import FilterSet

from .models import Vendor


class VendorFilter(FilterSet):
    
    class Meta:
        model = Vendor
        fields = ('name','location_footprint','supplier_channel')
        
    def __init__(self,*args,**kwargs):
        super(VendorFilter, self).__init__(*args,**kwargs)
        
        self.filters['name'].label ="Filter by Vendor Name"
        self.filters['location_footprint'].label ="Filter by Vendor Footprint"
        self.filters['supplier_channel'].label = "Filter by Supplier Channel"