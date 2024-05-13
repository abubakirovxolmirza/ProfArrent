from django.db.models.signals import pre_save
from django.dispatch import receiver
from .ai import chatbot_response
from .models import AI

@receiver(pre_save, sender=AI)
def update_gpt_result(sender, instance, **kwargs):
    created = kwargs.get('created', True)
    if created:
        gpt_result = chatbot_response(instance.result)
        instance.gpt_result = gpt_result


    