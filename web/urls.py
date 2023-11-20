from django.urls import path
from web.views import main_view, registration_view, auth_view, logout_view, create_note_view, \
    create_photo_view, PhotoListView, list_notes_view

urlpatterns = [
    path('', main_view, name='main'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('create_note/', create_note_view, name='create_note'),
    path('create_photo/', create_photo_view, name='create_photo'),
    path('photos/', PhotoListView.as_view(), name='photo_list'),
    path('list_notes/', list_notes_view, name='list_notes'),

]
