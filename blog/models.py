from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from unidecode import unidecode


class Tag(models.Model):
    name = models.CharField(verbose_name="标签名", max_length=30)

    class Meta:
        db_table = "tag"
        verbose_name = "分类标签"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField("博客题目", max_length=50, unique=True)
    slug = models.SlugField("slug", max_length=200, blank=True)
    content = RichTextUploadingField("博客内容")
    belong = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    create_date = models.DateField("创建时间", auto_now_add=True, null=True)
    edit_date = models.DateField("修改时间", auto_now=True, null=True)
    visits = models.PositiveIntegerField("访问量", default=0)

    class Meta:
        db_table = "blog"
        verbose_name = "博客"

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(unidecode(self.title))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def visited(self):   # 访问量加一
        self.visits += 1
        self.save(update_fields=['visits'])
