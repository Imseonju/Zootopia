from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class LLuser(AbstractUser):
    refresh = models.IntegerField(default = 0, verbose_name='접속횟수')

    def countup(self):
        self.refresh += 1
        self.save()
        return self.refresh

class Character(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목' )
    photo = models.ImageField(upload_to = '%d')
    number = models.IntegerField(primary_key=True, verbose_name='캐릭터번호')
    name = models.CharField(max_length=20, verbose_name='이름')
    gender = models.CharField(max_length= 10, verbose_name='성별')
    job = models.CharField(max_length=10, verbose_name='직업')
    species = models.CharField(max_length=10, verbose_name='동물 분류')

    class Meta:
        verbose_name_plural = '캐릭터'