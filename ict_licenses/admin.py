from django.contrib import admin
from .models import License, Renewal
# Register your models here.


 
@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ['name','contract','software_category','start_date',
                    'next_renewal_date','current_cost','owner','is_closed']

@admin.register(Renewal)
class RenewalAdmin(admin.ModelAdmin):
    list_display = ['license','renewal_date','amount']

