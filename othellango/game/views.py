
from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from . import game_handling

# Create your views here.

def game_index(request):
	return render(request, 'game/game_index.html')

def disc_moved(request):
	if request.method != 'POST':
		return HttpResponse(status=405)
	
	
	jsonBoard = request.POST.get("board")
	if jsonBoard is None:
		return HttpResponse(400)
	
	try:
		board = json.loads(request.POST.get("board"))
	except:
		return HttpResponse(422)
	lastPlayer = request.POST.get("lastPlayer")

	if lastPlayer in [0, 1]:
		return HttpResponse(422)
	
	lastPlayer = int(lastPlayer)
	
	nextPlayer = int(not lastPlayer)

	try:
		lastPlacedCoords = json.loads(request.POST.get("lastPlacedCoords"))
	except:
		return HttpResponse(422)

	pprint(board)
	print(lastPlayer, nextPlayer)

	game_handling.displayBoard(board)
	board = game_handling.checkBoard(board, lastPlayer, lastPlacedCoords)
	game_handling.displayBoard(board)
	board = game_handling.removeSquareType(board, -2)
	game_handling.displayBoard(board)
	board = game_handling.addPossibleMoves(board, nextPlayer)
	game_handling.displayBoard(board)
	winner = game_handling.checkForWin(board)
	
	

	# Placeholder.
	responseData = {
		'winner': winner,
        'new_board': board,
    }

	pprint(responseData)

	return JsonResponse(responseData)