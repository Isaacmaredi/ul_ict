from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
from ict_vendors.models import Vendor
from ict_accounts.models import Profile
from django.db.models import F, Value, DecimalField
from django.db.models.functions import Coalesce
from django.db.models.aggregates import Sum
# from profiles.models import Profile
from django.conf import settings
from datetime import datetime, date, timedelta
from django.utils import timezone
from decimal import Decimal

# Create your models here.
AGREEMENT_TYPE_CHOICES = [
    (None,'Select agreement type'),
    ('Master Service Agreement','Master Service Agreement'),
    ('Service Level Agreement','Service Level Agreement'), 
    ('Fixed Contract','Fixed Contract'),
    ('Subscription Agreement','Subscription Agreement'),
    ('Pay-per-Use','Pay-per-Use'),
]
# Create your models here.  
class Contract(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, 
                            max_length=300, verbose_name="Responsible Manager")
    supplier = models.ForeignKey(Vendor, related_name='vendors', 
                                on_delete=models.DO_NOTHING)
    total_value = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10, 
                                    verbose_name="Contract Value")
    agreement_type = models.CharField(verbose_name="Agreement Type" ,max_length=150, 
                                    choices=AGREEMENT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    # duration = models.IntegerField(blank=True, null=True)
    # status = models.CharField(max_length=300, default='Ok')
    date_signed = models.DateField(blank=True, null=True)
    ul_signatory = models.CharField(max_length=300, verbose_name="UL Signatory")
    supplier_signatory = models.CharField(max_length=300, verbose_name="Supplier Signatory")
    contract_document = models.FileField(upload_to='contracts/%Y/%F')
    comments = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=False)
    
    def __str__(self):  
        return self.name
    
    class Meta:
        ordering = ('-total_value',)
        
        
    def get_absolute_url(self):
        return reverse ('ict_contracts:contract-admin-detail', kwargs={'pk':self.pk})
    
    @property
    def duration(self):
        # duration_delta  = timedelta(months=12)
        if self.end_date:
            contract_duration_days= self.end_date - self.start_date
            contract_duration =int(str(contract_duration_days).split(' ',1)[0])/366
            duration = round(contract_duration)
        else:
            duration = None
        return duration

    @property
    def days_until_end(self, *args, **kwargs):
        today = date.today()
        if not self.end_date:
            days_until = -9999
        else:
            days = self.end_date - today
            days_until=int(str(days).split(' ')[0]) 
        return days_until

    @property
    def status(self, *args, **kwargs):
        if self.days_until_end > 365:  
            status_value = "Ok"
        elif self.days_until_end < 365 and self.days_until_end >= 180:
            status_value = "Attention"
        elif self.days_until_end < 180 and self.days_until_end >= 0:
            status_value = "Warning"
        elif self.days_until_end == -9999:
            status_value = "Perpertual"
        else:
            status_value = "Expired"
        return status_value
    
    @property
    def days_till_renewal(self):
        today = date.today()
        days_to_expiry = self.end_date - today
        days_to_expiry = str(days_to_expiry).split(' ',1)[0]
        int_days_to_expiry = int(days_to_expiry)
        return int_days_to_expiry
    
