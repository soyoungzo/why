from django.db import models
from django.contrib.auth.models import User
from main.models import Blog

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    post_like = models.ManyToManyField('main.Blog', blank=True, related_name='like_user')
    #blank=true 빈칸을 인식, 빈칸을 허용한다

    def __str__(self):
        return self.nickname

# Create your models here.
