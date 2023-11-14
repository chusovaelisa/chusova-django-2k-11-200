from django.shortcuts import render, redirect
from .forms import NoteForm
from django.contrib.auth.models import AnonymousUser
from datetime import datetime

from django.contrib.auth import get_user_model, authenticate, login, logout

from web.forms import RegistrationForm, AuthForm
from .models import HomeCategory, WorkCategory, FamilyCategory, ShopCategory

User = get_user_model()


def main_view(request):
    year = datetime.now().year
    return render(request,"web/main.html",{
        "year":year
    })


def registration_view(request):
    form = RegistrationForm
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user =  User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request,"web/registration.html",
                  {"form": form,"is_success": is_success
                   })


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None,"Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request,"web/auth.html",{"form": form})


def logout_view(request):
    logout(request)
    return redirect("main")


def note_add_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            if isinstance(request.user, AnonymousUser):
                form.instance.user_id = 1
            else:
                form.instance.user = request.user
            form.save()
            return redirect('some_success_url')
    else:
        form = NoteForm()

    return render(request, 'web/note.html', {'form': form})


def note_add_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            if isinstance(request.user, AnonymousUser):
                form.instance.user_id = 1
            else:
                form.instance.user = request.user

            form.instance.note_date = datetime.now().date()

            form.save()
            return redirect('create_note')
    else:
        form = NoteForm()

    return render(request, 'web/note.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import NoteForm
from django.contrib.auth.models import AnonymousUser
from datetime import datetime

def create_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            if isinstance(request.user, AnonymousUser):
                form.instance.user_id = 1
            else:
                form.instance.user = request.user

            form.instance.note_date = datetime.now().date()

            category_choice = form.cleaned_data['category']

            if category_choice == 'home':
                category, created = HomeCategory.objects.get_or_create(category_name='Дом')
            elif category_choice == 'work':
                category, created = WorkCategory.objects.get_or_create(category_name='Работа')
            elif category_choice == 'family':
                category, created = FamilyCategory.objects.get_or_create(category_name='Семья')
            elif category_choice == 'shop':
                category, created = ShopCategory.objects.get_or_create(category_name='Магазин')

            form.instance.home_category = category

            form.save()
            return redirect('create_note')
    else:
        form = NoteForm()

    return render(request, 'web/create_note.html', {'form': form})


