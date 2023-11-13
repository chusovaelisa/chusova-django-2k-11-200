from django.contrib.auth import get_user_model
from django import forms
from .models import Note, Category, Priority

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class NoteForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('дом', 'Дом'),
        ('работа', 'Работа'),
        ('семья', 'Семья'),
        ('магазин', 'Магазин')
    ]

    PRIORITY_CHOICES = [
        ('маловажно', 'Маловажно'),
        ('важно', 'Важно'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, initial='маловажно')
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Note
        fields = ['title', 'category', 'priority']