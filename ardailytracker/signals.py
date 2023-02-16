from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime


from .models import Detail

@receiver(pre_save, sender=Detail)
def update_allocation_Date(sender, instance, **kwargs):
    # if instance.assigned_To != instance._original_assigned_To:

    instance.allocation_Date = datetime.now().date() #timezone.now()