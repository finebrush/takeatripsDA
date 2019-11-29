from django.db import models
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey

from demo.cities.choices import SELECT_PART, SELECT_TYPE, SELECT_CATEGORY
# from django.db.models import manager
# from django.db.models.query import QuerySet
# Create your models here.

class Category(models.Model):
    large = models.CharField(_('대분류'), max_length=64)
    medium = models.CharField(_('중분류'), max_length=64)
    small = models.CharField(_('소분류'), max_length=64)

    def __str__(self):
        return self.large

class CLarge(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CMedium(models.Model):
    categorylarge = models.ForeignKey(CLarge, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CSmall(models.Model):
    objects = models.Manager()
    categorylarge = models.ForeignKey(CLarge, on_delete=models.CASCADE)
    # categorymedium = GroupedForeignKey(CMedium, "categorylarge")
    categorymedium = ChainedForeignKey(
        CMedium, # 연결 할 모델..
        chained_field="categorylarge", # 연결 할 자신의 필드..
        chained_model_field="categorylarge", # 연결 할 모델의 필드..
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
        )
    # area = ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # street = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TmpTest(models.Model):
    choices1 = models.IntegerField(choices=SELECT_PART, verbose_name='choices Large')

    @property
    def choicesel(self):
        return str(self.choices1) # 1, 2, 3...

    def __str__(self):
        return str(self.choices1) # 먹다/마시다, 보다, 자다 ...

class TmpAdd(models.Model):
    name = models.CharField(max_length=30)
    tmptest = models.ForeignKey(TmpTest, on_delete=models.CASCADE)