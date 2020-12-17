from .models import UserForRec
from django.forms import ModelForm, TextInput, Select


class UserForRecForm(ModelForm):
    class Meta:
        model = UserForRec
        fields = ['name', 'surname', 'patronymic', 'age', 'education', 'diplom', 'experience', 'recommendation']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша фамилия',
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше отчество',
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш возраст',
            }),
            "experience": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш опыт работы',
            }),

            "diplom": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш возраст',
            }, choices=(('1', '',), ('Красный', 'Красный',), ('Синий', 'Синий',))
            ),

            "education": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш возраст',
            }, choices=(
                ('1', '',), ('Полное высшее', 'Полное высшее',), ('Неполное высшее', 'Неполное высшее',), ('Среднее', 'Среднее',),
                ('Среднее-профессиональное', 'Среднее-профессиональное',))
            ),
            "recommendation": TextInput(attrs={
                'id': 'recommendation',
                'class': 'form-control'
            })

        }
