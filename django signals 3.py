from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
     if transaction.get_connection().in_atomic_block:
         print("Signal is running in the same transaction.")
     else:
         print("Signal is running outside the transaction.") 
from django.contrib.auth.models import User
from django.db import transaction
with transaction.atomic():
     user = User.objects.create(username='testuser')
