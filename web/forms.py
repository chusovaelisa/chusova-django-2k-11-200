from django.contrib.auth import get_user_model
from django import forms
from .models import Note, Photo, Category


User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["password2"]:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class NoteForm(forms.ModelForm):
    category = forms.ChoiceField(
        label="Категория",
        choices=Category.CategoryType.choices,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Note
        fields = [
            "title",
            "content",
            "category",
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "caption"]
