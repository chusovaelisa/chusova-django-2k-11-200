from django.urls import path
from web.views import (
    main_view,
    registration_view,
    auth_view,
    logout_view,
    create_note_view,
    create_photo_view,
    PhotoListView,
    create_category_view,
    edit_note_view, delete_note_view,
)

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("create_photo/", create_photo_view, name="create_photo"),
    path("photos/", PhotoListView.as_view(), name="photo_list"),
    path("create_note/", create_note_view, name="create_note"),
    path("edit_note/<int:note_id>/", edit_note_view, name="edit_note"),
    path("create_category/", create_category_view, name="create_category"),
    path('delete_note/<int:note_id>/', delete_note_view, name='delete_note'),

]
