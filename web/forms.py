from django.contrib.auth import get_user_model
from django import forms
from .models import Note, HomeCategory as Category, Priority
User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
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


from django import forms
from .models import Note, HomeCategory, WorkCategory, FamilyCategory, ShopCategory

class NoteForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('home', 'Дом'),
        ('work', 'Работа'),
        ('family', 'Семья'),
        ('shop', 'Магазин')
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, initial='work')

    class Meta:
        model = Note
        fields = ['title', 'category']
