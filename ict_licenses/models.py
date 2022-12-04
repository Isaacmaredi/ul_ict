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

LICENSE_TYPE_CHOICES = [
    (None, 'Select license type'),
    ('PERPERTUAL AND SUPPORT','Perpertual and Support'),
    ('SUPPORT AND MAINTENANCE','Support and Maintenance'),
    ('ANNUAL SUBSCRIPTION', 'Annual Subscription'),
    ('EULA','End user License Agreement'),   
    ('CLICK THROUGH','Click Through'),
]

RENEWAL_TERM_CHOICES = [
    (None, 'Select renewal terms'),
    ('Annual Renewal','Annual Renewal'),
    ('Once-Off','Once-Off'), 
    ('Contract Term Linked','Contract Term Linked'),
    ( 'Pepertual','Pepertual'),
]

SOFTWARE_CATEGORY_CHOICES = [
    (None,'Select software category'),
    ('Productivity','Productivity'),
    ('Enterprise Resource Planning','Enterprise Resource Planning'),
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
    (None,'Select user base'),
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

RENEWAL_STATUS_CHOICES = [
    ('Not Started','Not Started'),
    ('Supplier Invitation','Supplier Invitation'),
    ('Purchase Request','Purchase Request'),
    ('Purchase Order','Purchase Order'),
    ('Invoice', 'Invoice'),
    ('Paid','Paid'),
]

PRICING_MODEL_CHOICES = [
    (None,'Select pricing model'),
    ('Support Retainer','Support Retainer'),
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
                                    related_name='contract')
    software_category = models.CharField(verbose_name="Software Category", max_length=250, 
                                            choices=SOFTWARE_CATEGORY_CHOICES)
    renewal_term = models.CharField(verbose_name="Renewal Term", max_length=250, 
                                        choices=RENEWAL_TERM_CHOICES)
    pricing_model = models.CharField(verbose_name="Pricing Model" ,max_length=200, 
                                        choices=PRICING_MODEL_CHOICES)
    start_date = models.DateField(verbose_name="Inception Date", null=True, blank=True)
    next_renewal_date = models.DateField(verbose_name="Next Renewal Date" ,blank=True, 
                                            null=True, editable=False)
    current_cost = models.DecimalField(default=Decimal('0.0'), decimal_places=2,
                                        max_digits=10, verbose_name="Current Cost")
    renewal_status = models.CharField(verbose_name="Renewal Status", max_length=250, 
                                        default="Not Started", choices=RENEWAL_STATUS_CHOICES)
    service_provider = models.ForeignKey(Vendor, verbose_name="Service Provider", 
                                            on_delete=models.CASCADE, related_name='vendor')
    user_base = models.CharField(verbose_name="User Base" ,max_length=250, 
                                    choices=USER_BASE_CHOICES)
    num_admin_users = models.PositiveIntegerField(verbose_name="Number of Admin Users", 
                                                    null=True, blank=True)
    num_end_users = models.PositiveIntegerField(verbose_name="Number of End Users", 
                                                null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='licenses')
    is_closed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ('-created',)
        
    def get_absolute_url(self):
        return reverse ('ict_licenses:license-admin-detail', kwargs={'pk':self.pk})
    
    def save(self, *args, **kwargs):
        renewal_delta = timedelta(days=365)
        if self.start_date:
            self.next_renewal_date = self.start_date + renewal_delta
        super(License,self).save(*args, **kwargs)
        
    @property
    def days_till_renewal(self):
        today = date.today()
        days_till = self.next_renewal_date - today
        days_until = str(days_till).split(' ',1)[0]
        int_days_until = int(days_until)
        return int_days_until
    
