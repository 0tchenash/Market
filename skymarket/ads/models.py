from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ads_images/', default=None, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title



class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.title    
