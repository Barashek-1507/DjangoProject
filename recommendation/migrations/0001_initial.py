# Generated by Django 3.1.4 on 2020-12-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserForRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Ваша фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Ваше отчество')),
                ('age', models.IntegerField(verbose_name='Ваш возраст')),
                ('diploma', models.CharField(max_length=50, verbose_name='Диплом')),
                ('education', models.CharField(max_length=50, verbose_name='Образование')),
                ('experience', models.IntegerField(verbose_name='Стаж работы')),
            ],
            options={
                'verbose_name': 'Пользователь для рекомендации',
                'verbose_name_plural': 'Пользователи для рекомендации',
            },
        ),
    ]
