from email.policy import default
from tabnanny import verbose
from django.db import models
from datetime import datetime
from PIL import Image

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)

    class Meta(object):
        verbose_name_plural = 'Комнаты'


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    class Meta(object):
        verbose_name_plural = 'Сообщения'

        def __str__(self):
            return f'{self.user}'


class Meetings(models.Model):
    title = models.CharField('Заголовок', max_length=30, default=False)
    description = models.TextField('Краткое описание', default=False)
    image = models.ImageField('Фото', default=False)

    class Meta(object):
        verbose_name_plural = 'Встречи'

    def __str__(self):
        return f'{self.title}'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.CharField(max_length=255)

    class Meta(object):
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'
