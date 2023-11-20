from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .forms import RegistrationForm, AuthForm, NoteForm, PhotoForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import Note, Photo, Category
from django.views.generic import ListView

User = get_user_model()


def main_view(request):
    year = datetime.now().year
    return render(request, "web/main.html", {"year": year})


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            is_success = True
    return render(
        request, "web/registration.html", {"form": form, "is_success": is_success}
    )


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main")


def create_note_view(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("list_notes")
    else:
        form = NoteForm()

    return render(request, "web/create_note.html", {"form": form})


from PIL import Image


def create_photo_view(request):
    if request.method == "POST":
        form = PhotoForm(
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()

            img = Image.open(photo.image.path)

            return redirect("photo_list")

    else:
        form = PhotoForm()

    return render(request, "web/create_photo.html", {"form": form})


class PhotoListView(ListView):
    model = Photo
    template_name = "photo_list.html"
    context_object_name = "photos"


def list_notes_view(request):
    notes = Note.objects.all()
    return render(request, "web/list_notes.html", {"notes": notes})
