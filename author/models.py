from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nick = models.CharField("昵称", max_length=10)
    tel = models.CharField('电话', max_length=20, blank=True)

    class Meta:
        db_table = 'author'
        verbose_name = "作者"   # admin中的菜单名称。

    def __str__(self):
        return self.user
