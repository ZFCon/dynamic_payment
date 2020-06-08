from django.apps import AppConfig


class UserappConfig(AppConfig):
    name = 'UserApp'

    # def ready(self):
    #     from .signals import collect_transaction
