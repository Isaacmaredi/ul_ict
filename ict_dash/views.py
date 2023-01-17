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
    
    contract_values = Contract.objects.values_list('total_value').order_by('-total_value')
    print('*'*75)
    print(contract_values)
    print('*'*75)
    contract_value_list = [int(item[0]) for item in contract_values]
    
    
    # int_list = [int(x[0]) for x in total_values.values_list()]
    print('='*75)
    print('AMOUNTS ARE', contract_value_list)
    print('='*75)
    contract_names = Contract.objects.values_list('name').order_by('-total_value')
    
    contract_name_list = [item[0] for item in contract_names]
    print('NAMES ARE: ', contract_name_list)
    
    
   
    
    context = {
        'num_contracts': num_contracts,
        'num_licenses': num_licenses,
        'num_projects': num_projects,
        'num_vendors': num_vendors,  
        'num_users': num_users,
        'contract_name_list':contract_name_list,
        'contract_value_list':contract_value_list,
    }
    return render(request, 'ict_dash/dashboard.html', context)
    
 
class ContractValueView(TemplateView):
    model = Contract
    template_name = "ict_dash/dash.html"
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(ContractValueView, self).get_context_data(*args, **kwargs)
        
        context['contract_name_list'] = [item[0] for item in Contract.objects.values_list('name').order_by('-total_value')]
        context['contract_value_list'] = [int(item[0]) for item in Contract.objects.values_list('total_value').order_by('-total_value')]
        return context