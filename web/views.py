from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from .forms import (
    RegistrationForm,
    AuthForm,
    PhotoForm,
    NoteForm,
    CategoryForm,
    NoteFilterForm,
)
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import Photo, Category, Note
from django.views.generic import ListView
from PIL import Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


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


def create_note_view(request, note_id=None):
    notes = Note.objects.filter(user=request.user)
    categories = Category.objects.all()

    filter_form = NoteFilterForm(request.GET)
    filter_form.is_valid()
    filters = filter_form.cleaned_data

    if filters["search"]:
        notes = notes.filter(title=filters["search"])

    if filters["category"]:
        notes = notes.filter(category=filters["category"])

    if filters["sort_by"] == "alphabetical":
        notes = notes.order_by("title")
    elif filters["sort_by"] == "date_added":
        notes = notes.order_by("note_date")

    paginator = Paginator(notes, 10)
    page = request.GET.get("page")

    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    category_form = CategoryForm()

    if note_id:
        note_instance = get_object_or_404(Note, id=note_id)
        note_form = NoteForm(request.POST or None, instance=note_instance)
    else:
        note_instance = None
        note_form = NoteForm(request.POST or None, initial={"user": request.user})

    if request.method == "POST":
        if "add_note" in request.POST:
            if note_form.is_valid():
                note_instance = note_form.save(commit=False)
                note_instance.user = request.user
                note_instance.save()

                messages.success(request, "Заметка успешно сохранена")

                if note_id:
                    existing_note = get_object_or_404(Note, id=note_id)
                    existing_note.delete()  # Удаление существующей заметки

                return redirect("main")
        elif "add_category" in request.POST:
            return redirect("create_category")

    return render(
        request,
        "web/create_note.html",
        {
            "note_form": note_form,
            "category_form": category_form,
            "notes": notes,
            "categories": categories,
            "user": request.user,
            "filter_form": filter_form,
        },
    )


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


def create_category_view(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect("create_note")

    else:
        category_form = CategoryForm()

    return render(request, "web/create_category.html", {"category_form": category_form})


def edit_note_view(request, note_id):
    note_instance = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Заметка успешно изменена")
            return redirect("main")
    else:
        form = NoteForm(instance=note_instance)

    return render(
        request,
        "web/edit_note.html",
        {"note_form": form, "user": request.user, "note_instance": note_instance},
    )


def delete_note_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        note.delete()
        return redirect("main")

    return render(request, "web/delete_note_confirm.html", {"note": note})
