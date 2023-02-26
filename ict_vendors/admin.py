from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_footprint','supplier_channel',
                    'contact_person','contact_phone','email')
    search_fields = ('name','location_footprint','contact_person')
    list_per_page = 15
    list_display_links = ('name',)
    
    # autocomplete_fields = ('location_footprint','supplier_channel')