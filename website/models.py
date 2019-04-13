from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField("标签名", max_length=30, unique=True)
    count = models.IntegerField("包含的数量", default=0, blank=True)

    class Meta:
        db_table = "category"
        verbose_name = "网址标签"

    def __str__(self):
        return self.name


class Website(models.Model):
    name = models.CharField("名称", max_length=50)
    url = models.URLField("链接", max_length=200, unique=True)
    describe = models.TextField("描述", max_length=150)
    category = models.ManyToManyField(Category, verbose_name="标签")
    create_date = models.DateField("创建时间", auto_now_add=True, null=True)
    edit_date = models.DateField("修改时间", auto_now=True, null=True)
    belong = models.ForeignKey(User, verbose_name="创建者", on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "website"
        verbose_name = "网址"

    def __str__(self):
        return self.name

