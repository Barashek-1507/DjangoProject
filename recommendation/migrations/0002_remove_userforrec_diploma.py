# Generated by Django 3.1.4 on 2020-12-16 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userforrec',
            name='diploma',
        ),
    ]
