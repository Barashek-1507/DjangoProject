# Generated by Django 3.1.4 on 2020-12-16 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_userforrec_diplom'),
    ]

    operations = [
        migrations.AddField(
            model_name='userforrec',
            name='recommendation',
            field=models.TextField(default='oOo', verbose_name='Ваши рекомендации'),
        ),
        migrations.AlterField(
            model_name='userforrec',
            name='diplom',
            field=models.CharField(max_length=50, verbose_name='Диплом'),
        ),
    ]
