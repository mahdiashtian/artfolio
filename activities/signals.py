from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from activities.models import ArtActivity
from activities.tasks import send_sms, send_email

User = get_user_model()


@receiver(post_save, sender=ArtActivity)
def send_notification_to_user(sender, instance: ArtActivity, created: bool, **kwargs):
    user: User = instance.user
    if user.phone_number:
        send_sms.delay(user.phone_number, f'فعالیت {instance.name} با موفقیت ثبت شد.')
    if user.email:
        send_email.delay(user.email, f'فعالیت {instance.name} با موفقیت ثبت شد.')
