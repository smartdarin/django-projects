
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
 
def user_saved_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5) 
    print("Signal handler finished.")
 
from django.contrib.auth.models import User
 
print("Saving user...")
user = User.objects.create(username='testuser')
print("User saved.")
