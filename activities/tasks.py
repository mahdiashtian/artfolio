from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from melipayamak import Api

SMS_USERNAME = settings.SMS_USERNAME
SMS_PASSWORD = settings.SMS_PASSWORD
SMS_FROM = settings.SMS_FROM
EMAIL_FROM = settings.EMAIL_HOST_USER

api = Api(SMS_USERNAME, SMS_PASSWORD)
sms = api.sms()


@shared_task
def send_sms(to, text):
    sms.send(to, SMS_FROM, text)


@shared_task
def send_email(to, text):
    subject = 'Artfolio'
    message = text
    recipient_list = [to]
    send_mail(subject, message, EMAIL_FROM, recipient_list)
