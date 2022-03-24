
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
	lastPlayer = request.POST.get("lastPlayer") # validate these
	nextPlayer = int(not lastPlayer)
	print(board, lastPlayer, nextPlayer)
	
	board = game_handling.checkBoard(board, lastPlayer)
	board = game_handling.addPossibleMoves(board, nextPlayer)
	winner = game_handling.checkForWin(board)

	# Placeholder.
	responseData = {
		'winner': winner,
        'new_board': board,
    }

	return JsonResponse(responseData)