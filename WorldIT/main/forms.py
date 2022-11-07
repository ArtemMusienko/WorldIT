from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from captcha.fields import CaptchaField, CaptchaTextInput
from .models import Profile, PostSystem
from django.forms import ModelForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Ваше имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Ваш пароль'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Ваше имя пользователя'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Ваш пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Подтверждение вашего пароля'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': 'Ваш e-mail'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

CONTACT_CHOICES= [
    ('Реклама', 'Реклама'),
    ('Партнерство', 'Партнерство'),
    ('Прочее', 'Прочее'),
    ]

class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше ФИО', widget=forms.TextInput(attrs={'class': 'formm', 'placeholder': 'Фамилия Имя Отчество'}))
    tema = forms.CharField(label='Ваша тема проекта',widget=forms.Select(attrs={'class': 'formm', 'placeholder': 'Тема проекта'}, choices=CONTACT_CHOICES))
    number = forms.CharField(label='Ваш номер телефона', widget=forms.TextInput(attrs={'class': 'formm', 'placeholder': 'Номер телефона формата +7'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'formm', 'placeholder': 'Сообщение о сотрудничестве'}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': 'field', 'placeholder': 'Ответ к математической задаче'}))

SALE_CHOICES= [
    ('Discord', 'Discord'),
    ('VK', 'VK'),
    ('1C', '1C'),
    ('Telegram', 'Telegram'),
    ]

class SaleForm(forms.Form):
    name = forms.CharField(label='Ваше ФИО', widget=forms.TextInput(attrs={'class': 'formm', 'placeholder': 'Фамилия Имя Отчество'}))
    tema = forms.CharField(label='Ваша тема проекта', widget=forms.Select(attrs={'class': 'formm', 'placeholder': 'Тема проекта'}, choices=SALE_CHOICES))
    number = forms.CharField(label='Ваш номер телефона', widget=forms.TextInput(attrs={'class': 'formm', 'placeholder': 'Номер телефона формата +7'}))
    message = forms.CharField(label='Ваше описание проекта', widget=forms.Textarea(attrs={'class': 'formm', 'placeholder': 'Описание проекта'}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': 'field', 'placeholder': 'Ответ к математической задаче'}))

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Ваше имя пользователя'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': 'Ваш e-mail'}))
    first_name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Ваше фамилия', widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Фамилия'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label='Фотография')

    class Meta:
        model = Profile
        fields = ['image']

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput
    (attrs={'class': 'field', 'placeholder': 'Введите старый пароль', 'type': 'password'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput
    (attrs={'class': 'field', 'placeholder': 'Введите новый пароль', 'type': 'password'}))
    new_password2 = forms.CharField(label='Повтор нового пароля', widget=forms.PasswordInput
    (attrs={'class': 'field', 'placeholder': 'Введите ещё раз новый пароль', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class PostSystemForm(ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Напишите заголовок'}))
    content = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'class': 'field', 'placeholder': 'Напишите отзыв'}))

    class Meta:
        model = PostSystem
        fields = ['title', 'content']
