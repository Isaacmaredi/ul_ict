from django.contrib import admin

from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['name','owner','created_by','total_value','start_date','end_date','status']
    exclude = ('created_by',)
    def save_model(self, request, obj, form, change,):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
