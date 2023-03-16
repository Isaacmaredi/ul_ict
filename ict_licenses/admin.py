from django.contrib import admin
from .models import License, LicenseRenewal
# Register your models here.


 
@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ['name','contract','software_category','start_date',
                    'next_renewal_date','current_cost','owner','is_closed']
    raw_id_fields = ['contract']

@admin.register(LicenseRenewal)
class LicenseRenewalAdmin(admin.ModelAdmin):
    list_display = ['license','renewal_date','pr_number','po_number','renewal_amount','is_paid','renewal_status']

