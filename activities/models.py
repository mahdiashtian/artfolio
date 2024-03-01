from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from utils.file import upload_image_path

User = get_user_model()


class ArtActivity(models.Model):
    class TypeChoices(models.TextChoices):
        ONLINE = 'ONLINE', ('آنلاین')
        OFFLINE = 'OFFLINE', ('آفلاین')

    class ActivityChoices(models.TextChoices):
        attending_the_exhibition = 'attending_the_exhibition', ('حضور در نمایشگاه')
        create_work = 'create_work', ('خلق اثر')
        holding_exhibition = 'holding_exhibition', ('برگزاری نمایشگاه')
        holding_training_class = 'holding_training_class', ('برگزاری کلاس آموزشی')
        foreign_exhibition = 'foreign_exhibition', ('نمایشگاه خارجی')
        other = 'other', ('سایر')

    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', ('در انتظار')
        ACCEPTED = 'ACCEPTED', ('تایید شده')
        REJECTED = 'REJECTED', ('رد شده')

    name = models.CharField(max_length=100, verbose_name='نام فعالیت')
    description = models.TextField(verbose_name='توضیحات')
    type = models.CharField(max_length=10, choices=TypeChoices.choices, default=TypeChoices.ONLINE, verbose_name='نوع')
    amount_of_value = models.PositiveIntegerField(verbose_name='مقدار ارزش')
    activity_date = models.DateTimeField(verbose_name='تاریخ فعالیت', default=timezone.now)
    activity = models.CharField(max_length=50, choices=ActivityChoices.choices, verbose_name='نوع فعالیت')
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING,
                              verbose_name='وضعیت')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_user',
                             limit_choices_to={'is_staff': False}, verbose_name='کاربر')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'activities'
        ordering = ('-activity_date',)
        verbose_name = 'فعالیت هنری'
        verbose_name_plural = 'فعالیت های هنری'


class Photo(models.Model):
    image = models.ImageField(upload_to=upload_image_path, verbose_name='عکس')
    activity = models.ForeignKey(ArtActivity, on_delete=models.CASCADE, related_name='photo_activity')

    def __str__(self):
        return f'Photo: {self.activity.name}'

    class Meta:
        app_label = 'activities'
        verbose_name = 'تصویر'
        verbose_name_plural = 'گالری تصاویر'
