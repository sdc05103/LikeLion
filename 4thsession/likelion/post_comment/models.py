from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    userid = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128, null=True)
    major = models.CharField(max_length=128, null=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=128, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='이미지')
    content = models.TextField(verbose_name='내용', null=True)
    likes = models.IntegerField(verbose_name='좋아요', default=0)
    created_at = models.DateTimeField(verbose_name='작성일', default=timezone.now)
    
class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(verbose_name='내용', null=True)
    likes = models.IntegerField(verbose_name='좋아요', default=0)
    created_at = models.DateTimeField(verbose_name='작성일', default=timezone.now)

