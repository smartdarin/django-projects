from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading 
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
     print(f"Signal handler thread: {threading.current_thread().name}")
     from django.contrib.auth.models import User
     import threading
     print(f"Main thread: {threading.current_thread().name}")
     user = User.objects.create(username='testuser')
