from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'formm',
                'placeholder': ' Название вакансии'
            }),
            "anons": Textarea(attrs={
                'class': 'formm',
                'placeholder': ' Анонс вакансии'
            }),
            "full_text": Textarea(attrs={
                'class': 'formm',
                'placeholder': ' Текст вакансии'
            }),
            "date": DateTimeInput(attrs={
                'class': 'formm',
                'placeholder': ' Дата публикации'
            }),
        }