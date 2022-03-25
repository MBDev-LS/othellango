
import copy
import math
from random import randint

"""
testBoard = [[-1 for i in range(0, 8)] for j in range(3)]
testBoard.append([1, -2, 1, 0, 1, -1, -1, -1])
testBoard.append([-1, -1, -1, 1, 0, -1, -1, -1])
testBoard += [[-1 for i in range(0, 8)] for j in range(3)]

# testBoard = []
# testBoard.append([-1, -1, -1, 0, 1, -1, -1, -1])
# testBoard += [[-1 for i in range(0, 8)] for j in range(2)]
# testBoard.append([-1, -1, -1, 0, 1, -1, -1, -1])
# testBoard.append([-1, -1, -1, 1, 0, -1, -1, -1])
# testBoard += [[-1 for i in range(0, 8)] for j in range(2)]
# testBoard.append([1, -1, -1, 1, 0, -1, -1, -1])

"""

emojiLookupDict = {
	'🟩': -1,
	'⚪': 0,
	'⚫': 1
}

def displayBoard(board: list) -> None:
	outputString = ''
	
	for y in range(0, len(board)):
		for x in range(0, len(board)):
			if board[y][x] == -1:
				outputString += '🟩'
			elif board[y][x] == 0:
				outputString += '⚪'
			elif board[y][x] == 1:
				outputString += '⚫'
			elif board[y][x] == -2:
				outputString += '⭕'
			else:
				outputString += '❌'
		outputString += '\n'
	
	print(outputString)

def checkLinesFromPoint(board: list, pointCoords: tuple, lineModY: int, lineModX: int, playerBeingChecker: int):
	
	checkingX = pointCoords[0]
	checkingY = pointCoords[1]

	lines = []

	while checkingY >= 0 and checkingY < len(board):
		ranX = False
		while checkingX >= 0 and checkingX < len(board[checkingY]): # Check if (checkingY, checkingX)/[checkingY, checkingX] == pointCoords
			if not (checkingY >= 0 and checkingY < len(board)):
				break
			ranX = True

			checkBoard = copy.deepcopy(board)
			checkBoard[checkingY][checkingX] = 'TEST'
			displayBoard(checkBoard)

			if board[checkingY][checkingX] == -1: # This broke it
				break
			
			if board[checkingY][checkingX] == playerBeingChecker:
				if (checkingX, checkingY) != pointCoords:
					lines.append((checkingX, checkingY))

			checkingX += lineModX
			checkingY += lineModY

			if lineModX == 0 or checkingY >= len(board): # 
				break
			# elif checkingX >= len(board[checkingY]):
			# 	break
		
		if ranX is not True:
			checkingY += lineModY

		if checkingY >= len(board):
			break
		elif checkingX >= len(board[checkingY]):
			break

		if lineModY == 0 or board[checkingY][checkingX] == -1:
			break
	
	if len(lines) == 0:
		return board
	
	linesWithInfo = [{
		'end': lineEnd,
		'length': math.sqrt((lineEnd[0]-pointCoords[0])**2+(lineEnd[1]-pointCoords[1])**2)
	} for lineEnd in lines]

	# sortedLinesWithInfo = sorted(linesWithInfo, key=lambda k : k['length'])

	yForPlacement = pointCoords[1]
	xForPlacement = pointCoords[0]
	newBoard = copy.deepcopy(board)

	endToUseIndex = 1 if len(linesWithInfo) > 1 else 0
	while True:
		newBoard[yForPlacement][xForPlacement] = playerBeingChecker
		if (xForPlacement, yForPlacement) == linesWithInfo[endToUseIndex]['end']:
			break
		yForPlacement += lineModY
		xForPlacement += lineModX
	
	return newBoard

def merge_boards(boardList: list, discPreference: int) -> list:
	newBoard = [[-1 for i in range(0, 8)] for j in range(8)]
	for board in boardList:
		if board[4][4] == 1:
			print('FOUND BLACK')

		for y in range(0, len(board)):
			for x in range(0, len(board[y])):
				if board[y][x] != -1:
					if board[y][x] == discPreference or newBoard[y][x] == -1:
						newBoard[y][x] = board[y][x]

	return newBoard


def checkBoard(board: list, playerBeingChecker: int, lastPlacedCoords) -> list:
	"""
	Takes in board, returns board with flips made.
	"""
	newBoardList = []


	for yMod in range(-1, 2):
		for xMod in range(-1, 2):
			if yMod == 0 and xMod == 0:
				continue
			newBoardList.append(checkLinesFromPoint(board, lastPlacedCoords, yMod, xMod, playerBeingChecker))
	
	return merge_boards(newBoardList, playerBeingChecker) if len(newBoardList) > 0 else board

def linearPossibleMoveCheck(board: list, pointCoords: tuple, yLineMod: int, xLineMod: int, playerToMove: int, representativeInt: int) -> list:
	print(pointCoords, yLineMod, xLineMod)
	checkingX = pointCoords[0]
	checkingY = pointCoords[1]

	newBoard = copy.deepcopy(board)

	opposition = int(not playerToMove)
	coveredOpposition = False

	runY = True

	while checkingY >= 0 and checkingY < len(board) and runY is True:
		ranX = False
		runX = True
		while checkingX >= 0 and checkingX < len(board[checkingY]) and runX is True:
			
			if not (checkingY >= 0 and checkingY < len(board)):
				break
			ranX = True
			
			checkBoard = copy.deepcopy(board)
			checkBoard[checkingY][checkingX] = 'TEST'
			displayBoard(checkBoard)

			if board[checkingY][checkingX] == playerToMove:
				coveredOpposition = False
			
			if board[checkingY][checkingX] == opposition:
				coveredOpposition = True
			elif board[checkingY][checkingX] == -1:
				
				if coveredOpposition == True:
					print('NEW')
					displayBoard(newBoard)
					newBoard[checkingY][checkingX] = representativeInt
					return newBoard
				else:
					return newBoard

			checkingX += xLineMod
			checkingY += yLineMod

			if xLineMod == 0:
				runX = False

			if checkingY >= len(board):
				break
			elif checkingX >= len(board[checkingY]):
				break
		
		# if checkingY >= len(board):
		# 		break
		# elif checkingX >= len(board[checkingY]):
		# 	break
		
		if ranX is not True:
			checkingY += xLineMod

		if yLineMod == 0:
			runY = False
	
	return newBoard

def addPossibleMoves(board: list, playerToMove: int, representativeInt: int=-2) -> list:
	"""
	Takes board, player to move and an integer to represent
	possible moves. Returns board with given integer in
	the places where the player can place their disc.
	"""
	newBoardList = []

	for y in range(0, len(board)):
		for x in range(0, len(board[y])):
			if board[y][x] != playerToMove:
				continue
			
			for yMod in range(-1, 2):
				for xMod in range(-1, 2):
					if yMod == 0 and xMod == 0:
						continue 
					newBoardList.append(linearPossibleMoveCheck(board, (x, y), yMod, xMod, playerToMove, representativeInt))
	
	return merge_boards(newBoardList, representativeInt)

def checkForWin(board: list) -> int:
	"""
	Takes board, returns -1 if the game is still in progress,
	returns 0 if white has won, 1 is black has one and 2 if
	it is a draw.
	"""
	if not len(set([place for row in board for place in row])) <= 2:
		return -1
	
	flatBoard = [place for row in board for place in row]
	if 0 in flatBoard and 1 in flatBoard:
		if flatBoard.count(0) == flatBoard.count(1):
			return 2
		elif flatBoard.count(0) > flatBoard.count(1):
			return 0
		else:
			return 1
	elif 0 in flatBoard:
		return 0
	elif 1 in flatBoard:
		return 1
	
	return -1

def removeSquareType(board: list, squareTypeToRemove: int, squareTypeToReplaceWith: int=-1) -> list:

	for y in range(len(board)):
		for x in range(len(board[y])):
			if board[y][x] == squareTypeToRemove:
				board[y][x] = squareTypeToReplaceWith

	return board

"""
displayBoard(testBoard)

testBoard = checkBoard(testBoard, 1)
print(testBoard)
displayBoard(testBoard)
"""

# displayBoard(addPossibleMoves(testBoard, 1))
# testBoard = [[0 for i in range(0, 8)] for j in range(4)]
# testBoard += [[1 for i in range(0, 8)] for j in range(4)]
# displayBoard(testBoard)
# print(checkForWin(testBoard))

tBoard = [[-1, -1, -1, -1, -1, -1, -1, -1],
		[-1, -1, -1, -1, -1, -1, -1, -1],
		[-1, -1, -1, -2, -1, -1, -1, -1],
		[-1, -1, -2, 0, 1, -1, -1, -1],
		[-1, -1, -1, 1, 0, -2, -1, -1],
		[-1, -1, -1, -1, -2, -1, -1, -1],
		[-1, -1, -1, -1, -1, -1, -1, -1],
		[-1, -1, -1, -1, -1, -1, -1, -1]]

# board = checkBoard(tBoard, 1)
# displayBoard(board)
# board = addPossibleMoves(tBoard, 0)
# displayBoard(board)
# winner = checkForWin(board)

# ttBoard = [[-1, -1, -1, -1, -1, -1, -1, -1],
#  [-1, -1, -1, -2, -1, -1, -1, -1],
#  [-1, 0, 1, 1, 1, 0, -1, -1],
#  [-2, -1, -2, 1, 1, -1, -1, -1],
#  [-2, 1, 1, 0, 1, 1, -2, -1],
#  [-1, -1, 0, 1, -2, -1, -1, -1],
#  [-1, 0, -1, 1, -1, -1, -1, -1],
#  [-1, -1, -1, -2, -2, -1, -1, -1]]

# displayBoard(ttBoard)
# ttBoard = removeSquareType(ttBoard, -2)
# displayBoard(ttBoard)
# ttBoard = checkBoard(ttBoard, 0, [1,2])
# displayBoard(ttBoard)
# ttBoard = addPossibleMoves(ttBoard, 1)
# displayBoard(ttBoard)
