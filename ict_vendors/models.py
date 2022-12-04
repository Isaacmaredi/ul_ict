from django.db import models
from django.urls import reverse


LOCATION_TYPE_CHOICES = [
    (None, 'Select company nationality'),
    ('LOCAL','Local'),
    ('MNC','Multinational Company'),
    ('FOREIGN','Foreign Based')        
]
    
SUPPLIER_CHANNEL_CHOICES = [
    (None,'Select supllier channel'),
    ('Direct-OEM','Direct-OEM'),
    ('INDIRECT-OEM','Indirect-OEM'), 
    ('LSP','Licensed Solutions Provider'),
    ('LCR','Local Certified Reseller'),
    ('LSS','Local Sole Supplier '),
]

class Vendor(models.Model):  
    name = models.CharField(max_length=200, verbose_name="Company Name")
    location_footprint = models.CharField(max_length=200, choices=LOCATION_TYPE_CHOICES, 
                                        verbose_name="Company Footprint")
    supplier_channel = models.CharField(max_length=200, choices = SUPPLIER_CHANNEL_CHOICES,
                                        verbose_name="Supplier Channel", blank=True, null=True)
    contact_person = models.CharField(max_length=200, default=None, verbose_name="Account Manager")
    contact_phone = models.CharField(max_length=15, verbose_name="Account Manager Phone")
    email = models.EmailField(max_length=100)
    physical_address = models.CharField(max_length=300, verbose_name="Physical Address", blank=True,null=True)
    postal_address = models.CharField(max_length=300, verbose_name="Postal Address", blank=True, null=True)
    executive_contact = models.CharField(max_length=200, blank=True,null=True,
                                        verbose_name="Executive Contact Person")
    exe_contact_phone = models.CharField(max_length=15,blank=True,null=True,
                                        verbose_name="Executive Contact Phone")
    logo = models.ImageField(default='logo.png', upload_to='company_logos/%Y', blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('ict_vendors:vendor-admin')
        
        
        
        


