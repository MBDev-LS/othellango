
import copy

testBoard = [[-1 for i in range(0, 8)] for j in range(3)]
testBoard.append([-1, -1, -1, 0, 1, -1, -1, -1])
testBoard.append([-1, -1, -1, 1, 0, -1, -1, -1])
testBoard += [[-1 for i in range(0, 8)] for j in range(3)]

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
			else:
				outputString += '❌'
		outputString += '\n'
	
	print(outputString)

def checkLinesFromPoint(board: list, pointCoords: tuple, lineModY: int, lineModX: int, playerBeingChecker: int):
	checkingY = pointCoords[0]
	checkingX = pointCoords[1]
	while checkingY >= 0 and checkingY < len(board):
		while checkingX >= 0 and checkingX < len(board):
			checkBoard = copy.deepcopy(board)
			checkBoard[checkingY][checkingX] = 'TEST'
			displayBoard(checkBoard)
			checkingX += lineModX

			if lineModX == 0:
				break
		
		if lineModY == 0:
			break
		checkingY += lineModY

def checkBoard(board: list, playerBeingChecker: int) -> list:
	for y in range(0, len(board)):
		for x in range(0, len(board[y])):
			for yMod in range(-1, 2):
				for xMod in range(-1, 2):
					if yMod == 0 and xMod == 0:
						continue
					checkLinesFromPoint(board, (x, y), yMod, xMod, playerBeingChecker)



checkBoard(testBoard, 1)
displayBoard(testBoard)