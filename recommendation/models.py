from django.db import models


class UserForRec(models.Model):
    name = models.CharField('Ваше имя', max_length=50)
    surname = models.CharField('Ваша фамилия', max_length=50)
    patronymic = models.CharField('Ваше отчество', max_length=50)
    age = models.IntegerField('Ваш возраст')
    education = models.CharField('Образование', max_length=50)
    diplom = models.CharField('Диплом', max_length=50)
    experience = models.IntegerField('Стаж работы')
    recommendation = models.TextField('Ваши рекомендации')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/recommendation/{self.id}'

    class Meta:
        verbose_name = 'Пользователь для рекомендации'
        verbose_name_plural = 'Пользователи для рекомендации'
