from django.db import models

# Create your models here.
from django.db import models
from decimal import Decimal
from django.urls import reverse
from ict_contracts.models import Contract
from ict_accounts.models import Account, Profile
from ict_vendors.models import Vendor

from datetime import datetime, date, timedelta
from django.utils import timezone
from decimal import Decimal

LICENSE_SERVICE_CHOICES = [
    ('Support and Maintenance','Support and Maintenance'),
    ('Annual Subscription', 'Annual Subscription'),
    ('EULA','End user License Agreement'),   
    ('Click Through','Click Through'),
]

RENEWAL_TERM_CHOICES = [ 
    ('Annual Renewal','Annual Renewal'),
    ('Once-Off','Once-Off'), 
    ('Term Contract','Term Contract'),
]

SOFTWARE_CATEGORY_CHOICES = [
    ('Productivity','Productivity'),
    ('Collaboration','Collaboration'),
    ('ERP','ERP'),
    ('CRM','CRM'),
    ('Learning Management System','Learning Management System'),
    ('Operating System','Operating System'),
    ('Database Management System','Database Management System'),
    ('Business Intelligence','Business Intelligence'),
    ('Data & Statistical Analytics','Data & Statistical Analytics'),
    ('Network Management','Network Management'),
    ('IT Service Management','IT Service Management'),
    ('Communication','Communication'),
    ('Collaboration','Collaboration'),
    ('Business Application','Business Application'),
    ('Academic Specialist Software','Academic Specialist Software'), 
]

USER_BASE_CHOICES = [
    ('Students','Students'),
    ('Academics','Academics'),
    ('Academics & Students','Academics & Students'),
    ('Admin Staff','Admin Staff'),
    ('Admin Staff & Students','Admin Staff & Students'),
    ('All Staff', 'All Staff'),
    ('All Staff & Students','All Staff & Students'),
    ('Academics Specialist','Academics Specialist'),
    ('ICT Staff','ICT Staff'),
]

PRICING_MODEL_CHOICES = [
    ('Retainer','Retainer'),
    ('Seats','Seats'),
    ('Cores','Cores'),
    ('Minutes','Minutes'),
    ('Storage', 'Storage'),
    ('Minutes & Storage','Minutes & Storage'),
]

class License(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()  
    contract = models.ForeignKey(Contract,on_delete=models.DO_NOTHING, null=True, blank=True, 
                                    related_name='licenses')
    software_category = models.CharField(verbose_name="Software Category", max_length=250, 
                                            choices=SOFTWARE_CATEGORY_CHOICES)
    renewal_term = models.CharField(verbose_name="Renewal Term", max_length=250, 
                                        choices=RENEWAL_TERM_CHOICES)
    pricing_model = models.CharField(verbose_name="Pricing Model" ,max_length=200, 
                                        choices=PRICING_MODEL_CHOICES)
    start_date = models.DateTimeField(verbose_name="Inception Date", null=True, blank=True)
    next_renewal_date = models.DateField(verbose_name="Next Renewal Date" ,blank=True, 
                                            null=True, editable=False)
    current_cost = models.DecimalField(default=Decimal('0.0'), decimal_places=2,
                                        max_digits=10, verbose_name="Current Cost")
    is_renewed = models.BooleanField(verbose_name="Renew License", default=False)
    service_provider = models.ForeignKey(Vendor, verbose_name="Service Provider", 
                                            on_delete=models.CASCADE, related_name='licenses')
    user_base = models.CharField(verbose_name="User Base" ,max_length=250, 
                                    choices=USER_BASE_CHOICES)
    num_admin_users = models.PositiveIntegerField(verbose_name="Number of Admin Users", 
                                                    null=True, blank=True)
    num_end_users = models.PositiveIntegerField(verbose_name="Number of End Users", 
                                                null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 
    owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='licenses')
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
 
    class Meta:
        ordering = ('-id',)
        
    def get_absolute_url(self):
        return reverse ('ict_licenses:license-detail', kwargs={'pk':self.pk})
    
    def save(self, *args, **kwargs):
        renewal_delta = timedelta(days=365)
        if self.start_date:
            self.next_renewal_date = self.start_date + renewal_delta
        super(License,self).save(*args, **kwargs)
        
    def update(self, *args, **kwargs):
        renewal_delta = timedelta(days=365)
        if self.renewal:
            self.next_renewal_date = self.start_date + renewal_delta
        super(License, self).update(*args, **kwargs)
                   
    @property
    def days_till_renewal(self):
        today = date.today()
        days_till = self.next_renewal_date - today
        days_until = str(days_till).split(' ',1)[0]
        int_days_until = int(days_until)
        return int_days_until  
    
class LicenseRenewal(models.Model):
    license = models.ForeignKey(License, on_delete=models.DO_NOTHING, related_name='renewals')
    renewal_date = models.DateField()
    renewal_amount = models.DecimalField(default=Decimal(0.0), max_digits=10, decimal_places=2)
    pr_number = models.CharField(max_length=30, null=True, blank=True)
    po_number = models.CharField(max_length=30, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    # renewal_count = models.IntegerField(default=0, verbose_name='Renewal Count')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.license} renewal on - {self.renewal_date} for {self.renewal_amount}'
    
    def save(self, *args, **kwargs):
        if self.po_number is not None:
            self.is_paid = True
        return super(LicenseRenewal, self).save(*args, **kwargs)
            
    
    @property
    def renewal_status(self):
        if self.pr_number == None and self.po_number == None:
            status = "Not started"
        elif self.pr_number  and self.po_number == None:
            status = "PR stage"
        elif self.po_number:
            status = "Renewal completed"
        return status
          
    
            
    
    