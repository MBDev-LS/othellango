from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def game_index(request):
	return render(request, 'game/game_index.html')