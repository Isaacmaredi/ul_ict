from unicodedata import name
from django.db import models
from django.db.models import Sum 
from django.urls import reverse
from datetime import datetime, date


from ict_vendors.models import Vendor
from ict_accounts.models import Account, Profile
from ict_contracts.models import Contract

# from datetime import datetime, date, timedelta
from django.utils import timezone
from decimal import Decimal

# Create your models here.
PROJECT_STATUS_CHOICES =[
    ('Not Started','Not Started'), 
    ('On Track', 'On Track'),
    ('Delayed','Delayed'), 
    ('Stopped','Stopped'),
    ('Completed','Completed')
]

PROJECT_ROLES_CHOICES =[
    ('Project Manager','Project Manager'),
    ('Technical Lead','Technical Lead'),
    ('Technical Support','Technical Support'),
    ('User Support','User Suport'),
    ('Business User', 'Business User'),
]

MILESTONE_STATUS_CHOICES = [
    ('Not Started','Not Started'),
    ('On Track','On Track'),
    ('Delayed', 'Delayed'),
    ('Stopped','Stopped'),
    ('Completed','Completed'),    
]

class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True,null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    total_cost = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10, 
                                    verbose_name="Total Project Value")
    # amount_outstanding = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10, 
                                # verbose_name="Amount Outstanding")
    service_provider = models.ForeignKey(Vendor, verbose_name="Service Provider", on_delete=models.DO_NOTHING,
                                        related_name="projects",blank=True, null=True)
    contract = models.ForeignKey(Contract, blank=True, null=True,on_delete=models.DO_NOTHING, related_name="projects")
    status = models.CharField(max_length=150, default= "Not Started", choices=PROJECT_STATUS_CHOICES)
    
    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
    # @property
    # def amount_outstanding(self):
    #     milestone_total = Project.objects.annotate( total = Sum('milestones__amount'))
    #     if self.amount_outstanding == 0:
    #         return self.total_cost - milestone_total
    #     else:
    #         return self.pramount_outstanding - self.milestone_total
    
    def get_absolute_url(self,**kwargs):
        return reverse('ict_projects:project-list')

class Team(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_role = models.CharField(max_length=150, choices=PROJECT_ROLES_CHOICES, 
                                    verbose_name="Project Role",default='Project Manager')
    project = models.ForeignKey(Project,null=True, blank=True, on_delete=models.DO_NOTHING, related_name="team")
    
    class Meta:
        verbose_name = ('Team Member')
        verbose_name_plural = ('Team Members')
    
    def __str__(self):
        return f'{self.name} - {self.project_role}'
    
    
class Milestone (models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, 
                                related_name='milestones')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(verbose_name='Start Date')
    planned_end_date = models.DateField(verbose_name='Planned End Date')
    actual_end_date = models.DateField(verbose_name='Actual End Date', blank=True, null=True)
    status = models.CharField(max_length=200, 
                            choices=MILESTONE_STATUS_CHOICES, 
                            default='Not Started')
    weight = models.PositiveIntegerField(verbose_name='Weight in %')
    amount = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10, 
                                    verbose_name="Milestone Amount")
    is_paid = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
    @property
    def update(self, *args, **kwargs):
        todate = date.now()
        if self.planned_end_date < todate and self.status!= "Completed":
            self.status = "Delayed"
        return super(Milestone, self).update(*args, **kwargs)
        
    
    # @property
    # def amount_outstanding(self):
    #     if self.project.amount_outstanding == 0 and self.is_paid:
    #         return self.project.total_cost - self.amount
    #     else:
    #         return self.project.amount_outstanding - self.amount
            


