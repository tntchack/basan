from django.db import models
from django.conf import settings
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default='default.jpg')
    ratio = models.IntegerField(default=10)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='Published')


class Message(models.Model):

    title = models.CharField(max_length=20)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    publish = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('Published', 'منتشر شده'),
        ('Draft', 'چک نویس')
    )
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default='Draft')

    TYPE_CHOICES = (
        ('Fixes', 'اصلاحات'),
        ('Upgrade', 'بروزرسانی ها')
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='fixes')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()


class Quran(models.Model):
    aye = models.TextField()
    tarjome = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    publish = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('Published', 'منتشر شده'),
        ('Draft', 'چک نویس')
    )
    status = models.CharField(choices=STATUS_CHOICES, default='Draft', max_length=30)

    def __str__(self):
        return self.ayah

    objects = models.Manager()
    published = PublishedManager()