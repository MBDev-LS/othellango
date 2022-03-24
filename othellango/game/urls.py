from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', view=views.game_index, name='game_index'),
	path('movedisc', view=views.disc_moved, name='movedisc')
]