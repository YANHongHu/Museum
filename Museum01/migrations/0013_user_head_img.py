# Generated by Django 2.1.4 on 2020-01-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Museum01', '0012_costume_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='head_img',
            field=models.CharField(default='../static/images/faa.jpg', max_length=32, verbose_name='头像'),
        ),
    ]
