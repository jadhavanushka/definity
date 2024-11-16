from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_word_definition, name='get_word_definition'),
]
