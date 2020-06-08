from django.apps import AppConfig


class OfflinepaymentConfig(AppConfig):
    name = 'Payment.OfflinePayment'
    # def ready(self):
    #     from .signals import *