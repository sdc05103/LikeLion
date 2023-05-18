# Generated by Django 4.2.1 on 2023-05-07 00:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post_comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='좋아요'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post_comment.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post_comment.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, verbose_name='내용'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='이미지'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(null=True, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post_comment.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='좋아요'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=128),
        ),
    ]
