from django.contrib import admin
from django.urls import path
from todoss.views import new_note_creation,note_delete,note_update,note_status


urlpatterns = [
    path('',new_note_creation,name="note"),
    path('update/<int:pk>',note_update,name="note_update"),
    path('delete/<int:pk>',note_delete,name="note_delete"),
    path('status/<int:pk>',note_status,name="note_status"),
    
]