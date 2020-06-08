from django.db.models.signals import pre_save, post_save, post_delete
from .models import Order, Transaction
from django.dispatch import receiver
from .utils import balance_transaction
 
 
@receiver(pre_save, sender=Order)
def price_with_promo(sender, instance,**kwargs):
    if instance.promo:
        instance.price = instance.promo.get_price(instance.thing.price)
    else:
        instance.price = instance.thing.price

@receiver(pre_save, sender=Order)
def make_paid(sender, instance,**kwargs):
    thething = instance.thing
    if instance.paid:
        thething.paid = True
        thething.save()


@receiver(post_save, sender=Transaction)
def collect_transaction_save(sender, instance, **kwargs):
    user = instance.user
    user.balance = balance_transaction(user)
    user.save()

@receiver(post_delete, sender=Transaction)
def collect_transaction_delete(sender, instance, **kwargs):
    user = instance.user
    user.balance = balance_transaction(user)
    user.save()