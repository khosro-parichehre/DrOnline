from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from wallet.models import Wallet

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_wallet(sender, instance, created, **kwargs):
    """
    signal to create user wallet
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Wallet.objects.create(user=instance)