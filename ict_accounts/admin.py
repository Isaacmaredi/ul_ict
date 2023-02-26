from django.contrib import admin
from .models import Account, Profile
# Register your models here.


admin.site.register(Account)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','unit','position')
    search_fields =('user',)