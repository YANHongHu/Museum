# Generated by Django 2.2.7 on 2019-11-23 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Museum01', '0004_auto_20191123_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='identity',
        ),
    ]
