## for Question 1, 2
# import time
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import MyModel

# @receiver(post_save, sender=MyModel)
# def my_signal_receiver(sender, instance, **kwargs):
#     print("Signal received. Starting delay...")
#     time.sleep(5)  
#     print("Signal receiver finished.")


# for Question 3
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import MyModel
import time

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received. Performing database action inside signal handler.")

    # Perform some database action inside the signal
    instance.name = "Modified in Signal"
    instance.save()

    
    if instance.name == "Error":
        raise Exception("Simulating error to trigger transaction rollback.")

    print("Signal handler completed successfully.")