from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class VK(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Описание', max_length=1500)
    full_text = models.TextField('Подробности')
    price = models.IntegerField('Стоимость')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/main/{self.id}'

    class Meta:
        verbose_name = 'ВК'
        verbose_name_plural = 'ВК'


class Discord(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Описание', max_length=1500)
    full_text = models.TextField('Подробности')
    price = models.IntegerField('Стоимость')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/main/{self.id}'

    class Meta:
        verbose_name = 'Дискорд'
        verbose_name_plural = 'Дискорд'


class Telegram(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Описание', max_length=1500)
    full_text = models.TextField('Подробности')
    price = models.IntegerField('Стоимость')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/main/{self.id}'

    class Meta:
        verbose_name = 'Телеграм'
        verbose_name_plural = 'Телеграм'


class OneC(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Описание', max_length=1500)
    full_text = models.TextField('Подробности')
    price = models.IntegerField('Стоимость')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/main/{self.id}'

    class Meta:
        verbose_name = '1C'
        verbose_name_plural = '1C'


class PostSystem(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
