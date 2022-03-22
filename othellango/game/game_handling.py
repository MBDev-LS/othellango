
import copy
import math

# testBoard = [[-1 for i in range(0, 8)] for j in range(3)]
# testBoard.append([-1, -1, -1, 0, 1, -1, -1, -1])
# testBoard.append([-1, -1, -1, 1, 0, -1, -1, -1])
# testBoard += [[-1 for i in range(0, 8)] for j in range(3)]
testBoard = []
testBoard.append([-1, -1, -1, 0, 1, -1, -1, -1])
testBoard += [[-1 for i in range(0, 8)] for j in range(2)]
testBoard.append([-1, -1, -1, 0, 1, -1, -1, -1])
testBoard.append([-1, -1, -1, 1, 0, -1, -1, -1])
testBoard += [[-1 for i in range(0, 8)] for j in range(2)]
testBoard.append([1, -1, -1, 1, 0, -1, -1, -1])

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
			else:
				outputString += '❌'
		outputString += '\n'
	
	print(outputString)

def checkLinesFromPoint(board: list, pointCoords: tuple, lineModY: int, lineModX: int, playerBeingChecker: int):
	# print(pointCoords, lineModY, lineModX)
	checkingX = pointCoords[0]
	checkingY = pointCoords[1]

	lines = []

	while checkingY >= 0 and checkingY < len(board):
		ranX = False
		while checkingX >= 0 and checkingX < len(board):
			if not (checkingY >= 0 and checkingY < len(board)):
				break
			ranX = True
			checkBoard = copy.deepcopy(board)
			checkBoard[checkingY][checkingX] = 'TEST'
			# displayBoard(checkBoard)
			if board[checkingY][checkingX] == playerBeingChecker:
				if (checkingX, checkingY) != pointCoords:
					lines.append((checkingX, checkingY))

			checkingX += lineModX
			checkingY += lineModY

			if lineModX == 0:
				break
		
		if ranX is not True:
			checkingY += lineModY

		if lineModY == 0:
			break
	
	if len(lines) == 0:
		return board
	
	linesWithInfo = [{
		'end': lineEnd,
		'length': math.sqrt((lineEnd[0]-pointCoords[0])**2+(lineEnd[1]-pointCoords[1])**2)
	} for lineEnd in lines]

	sortedLinesWithInfo = sorted(linesWithInfo, key=lambda k : k['length'])

	yForPlacement = pointCoords[1]
	xForPlacement = pointCoords[0]
	newBoard = copy.deepcopy(board)
	while True:
		newBoard[yForPlacement][xForPlacement] = playerBeingChecker
		if (xForPlacement, yForPlacement) == sortedLinesWithInfo[-1]['end']:
			break
		yForPlacement += lineModY
		xForPlacement += lineModX
	
	return newBoard

def merge_boards(boardList: list) -> list:
	newBoard = [[-1 for i in range(0, 8)] for j in range(8)]
	for board in boardList:
		for y in range(0, len(board)):
			for x in range(0, len(board[y])):
				if board[y][x] != -1:
					newBoard[y][x] = board[y][x]

	return newBoard


def checkBoard(board: list, playerBeingChecker: int) -> list:
	newBoardList = []

	for y in range(0, len(board)):
		for x in range(0, len(board[y])):
			if board[y][x] != playerBeingChecker:
				continue
			
			for yMod in range(-1, 2):
				for xMod in range(-1, 2):
					if yMod == 0 and xMod == 0:
						continue
					newBoardList.append(checkLinesFromPoint(board, (x, y), yMod, xMod, playerBeingChecker))
					displayBoard(board)
	
	return merge_boards(newBoardList)


displayBoard(testBoard)
displayBoard(checkBoard(testBoard, 1))
