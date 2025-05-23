'''  Yes, by default Django signals are part of the same transaction unless deferred using transaction.on_commit().  '''

# models.py
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def signal_handler(sender, instance, **kwargs):
    print("Signal handler running")
    raise Exception("Force rollback")
