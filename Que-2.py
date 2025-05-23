''' Yes, by default, Django signals run in the same thread as the caller. '''

# models.py
import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def signal_handler(sender, instance, **kwargs):
    print("Signal thread ID:", threading.get_ident())

# test_thread.py (or Django shell)
import threading
from myapp.models import MyModel

print("Main thread ID:", threading.get_ident())
MyModel.objects.create(name="Thread Test")
