from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', view=views.game_index, name='game_index'),
	path('movedisk', view=views.disk_moved, name='game_index')
]