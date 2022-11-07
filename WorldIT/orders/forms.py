from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя',
                            widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Напишите Ваше имя'}))
    last_name = forms.CharField(label='Фамилия',
                              widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Напишите Вашу фамилию'}))
    email = forms.EmailField(label='E-mail',
                                widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': 'Напишите Ваш e-mail'}))
    number = forms.CharField(label='Номер телефона',
                             widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Напишите Ваш номер телефона'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'number']

