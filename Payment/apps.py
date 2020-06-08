from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'Payment'

    def ready(self):
        from Payment.signals import price_with_promo, make_paid, collect_transaction_delete, collect_transaction_save
