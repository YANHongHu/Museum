# Generated by Django 2.2.7 on 2019-11-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Museum01', '0005_remove_user_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(default='', max_length=11, unique=True, verbose_name='电话'),
        ),
    ]
