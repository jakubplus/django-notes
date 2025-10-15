from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list_create, name='list'),
    path('<int:pk>/edit/', views.note_edit, name='edit'),
    path('<int:pk>/delete/', views.note_delete, name='delete'),
]
