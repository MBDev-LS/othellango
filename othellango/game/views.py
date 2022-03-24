
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from . import game_handling

# Create your views here.

def game_index(request):
	return render(request, 'game/game_index.html')

def disc_moved(request):
	if request.method != 'POST':
		return HttpResponse(status=405)
	
	board = request.POST.get("board")
	lastPlayer = request.POST.get("lastPlayer")

	# Placeholder.
	responseData = {
		'winner': 1,
        'new_board': [[-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, -1, -1, -1], [-1, -1, -1, 1, 0, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1]],
    }

	return JsonResponse(responseData)