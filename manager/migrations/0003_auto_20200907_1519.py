# Generated by Django 3.1.1 on 2020-09-07 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20200907_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='category',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='comment',
        ),
    ]