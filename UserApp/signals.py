from django.db.models.signals import pre_save, m2m_changed
from django.db.models import Sum
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()

# @receiver(pre_save, sender=User)
# def collect_transaction(sender, instance, **kwargs):
#     balance = instance.transactions.aggregate(Sum('order__price'))
#     print(balance)