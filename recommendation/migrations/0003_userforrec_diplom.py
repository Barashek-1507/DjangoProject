# Generated by Django 3.1.4 on 2020-12-16 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_remove_userforrec_diploma'),
    ]

    operations = [
        migrations.AddField(
            model_name='userforrec',
            name='diplom',
            field=models.CharField(default='Red', max_length=50, verbose_name='Диплом'),
        ),
    ]
