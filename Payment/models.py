from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Promo(models.Model):
    code = models.CharField(max_length=255)

    discount = models.PositiveIntegerField()
    discount_type = models.CharField(choices=[
        ('percent', 'Percent'),
        ('price', 'Price'),
    ], default='percent', max_length=20,
    help_text="The Precent choice convert the price like that (Price(20)-Price(20)*discount(25)%)=15. The Price choice convert the price like that (Price(20)-discount(15))=5.")

    def __str__(self):
        return self.code
    
    def get_price(self, price):
        if self.discount_type == 'percent':
            price -=  price*(self.discount/100)
        else:
            price -= self.discount
        
        if price < 0:
            price = 0 
  
        return price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thing = models.OneToOneField('Payment.TheThing', on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)

    price = models.FloatField(null=True, blank=True)
    promo = models.ForeignKey('Payment.Promo', on_delete=models.SET_NULL, null=True, blank=True)

    status = models.CharField(choices=[
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('canceled', 'Canceled'),
    ], max_length=20, default='pending')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.price)

class TheThingQuerySet(models.QuerySet):
    def paid(self):
        return self.filter(paid=True)

class TheThing(models.Model):
    paid = models.BooleanField(default=False)
    price = models.FloatField()

    objects = TheThingQuerySet.as_manager()

class PlaceHolder(TheThing):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    order = models.OneToOneField('Payment.Order', on_delete=models.CASCADE, related_name='transaction')
    
    transaction_type = models.CharField(choices=[
        ('transfer', 'Transfer'),
        ('received', 'Received'),
    ], max_length=20, default='transfer')
    created = models.DateTimeField(auto_now_add=True)