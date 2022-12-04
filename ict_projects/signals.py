# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Project, Milestone


# @receiver(post_save, sender=Milestone)
# def update_outstanding_amount(sender, instance, **kwargs):
#     project_instance = Project.objects.get(pk=instance.project_id)
#     if instance.is_paid:
        
#         print(type(project_instance.amount_outstanding))
#         print(project_instance.amount_outstanding)
        
#         if project_instance.amount_outstanding == 0: 
#             project_instance.amount_outstanding = project_instance.total_cost - instance.amount
#         else:
#             project_instance.amount_outstanding = project_instance.amount_outstanding - instance.amount
#     print('Amount Outstanding:',project_instance.amount_outstanding)
#     print('Project Total Value:',project_instance.total_cost)
#     print('Milestone Amount:',instance.amount)
#     project_instance.save()
    
# @receiver(post_save, sender=Milestone)
# def update_project_progress(sender, instance, **kwargs):
#     project_instance = Project.objects.get(pk=instance.project_id)
#     if instance.status == 'Completed' and instance.is_paid:
#         project_instance.progress = project_instance.progress + instance.weight 
#     print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#     print('Milestone Weight : ', instance.weight)
#     print('Project Progress : ', project_instance.progress)
#     project_instance.save()
      

    

