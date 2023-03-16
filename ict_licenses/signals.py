from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import License, LicenseRenewal


@receiver(post_save, sender=LicenseRenewal)
def renew_license(sender, instance, created, **kwargs):
   license_instance = License.objects.get(pk=instance.license.pk)
   if instance.po_number is not None:
       license_instance.start_date = instance.renewal_date
       license_instance.current_cost = instance.renewal_amount
       instance.is_paid = True
    #    instance.save()
       license_instance.save()
        