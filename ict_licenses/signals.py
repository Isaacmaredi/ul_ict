from django.db.models.signals import post_save
from django.dispatch import receiver
from ict_contracts.models import Contract
from .models import License   

@receiver(post_save, sender=License)    
def update_outstanding_amount(sender, instance, **kwargs):
    contract_instance = Contract.objects.get(pk=instance.contract_id)
    if instance.renewal_status == 'Paid' and contract_instance.amount_outstanding == 0 :
        contract_instance.amount_outstanding = contract_instance.total_value - instance.current_cost
    elif contract_instance.amount_outstanding > 0:
        contract_instance.amount_outstanding = contract_instance.amount_outstanding - instance.current_cost
    print('@@@@@@@@@@@@@@@@@@@@@@@')
    print('RENEWAL STATUS :  ',instance.renewal_status)
    print('CONTRACT TOTAL VALUE :',contract_instance.total_value )
    print ('CONTRACT OUTSTANDING : ' ,contract_instance.amount_outstanding)
    print ('CURRENT LICENSE COSTS : ', instance.current_cost)
    print('@@@@@@@@@@@@@@@@@@@@@@')
        
    contract_instance.save()