from django.shortcuts import render
from django.views.generic import TemplateView

from ict_contracts.models import Contract   
from ict_licenses.models import License
from ict_projects.models import Project
from ict_vendors.models import Vendor 
from ict_accounts.models import Account


# Create your views here.
def dash(request):
    
    num_contracts = Contract.objects.all().count()
    num_licenses = License.objects.all().count()
    num_projects = Project.objects.all().count()
    num_vendors = Vendor.objects.all().count()
    num_users = Account.objects.all().count()
    
    context = {
        'num_contracts': num_contracts,
        'num_licenses': num_licenses,
        'num_projects': num_projects,
        'num_vendors': num_vendors,
        'num_users': num_users,
    }
    return render(request, 'ict_dash/dashboard.html', context)
    