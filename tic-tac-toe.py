import random

gameOver = False
turnsTaken = 0

playerOne = input("Player 1, enter your name:  ")
playerOneSymbol = input(str(playerOne) + ", enter the symbol you'd like to use:  ")
if len (playerOneSymbol) > 1:
	playerOneSymbol = playerOneSymbol[0]
playerTwo = input("Player 2, enter your name:  ")
playerTwoSymbol = input(str(playerTwo) + ", enter the symbol you'd like to use:  ")

players = [playerOne, playerTwo]
symbols = [playerOneSymbol, playerTwoSymbol]
currentPlayer = players[0]
currentSymbol = symbols[0]

def resetBoard():
	global board
	board = [
		[" ", "1", "2", "3"], 
		["1", "?", "?", "?"],
		["2", "?", "?", "?"],
		["3", "?", "?", "?"]
		]

def printBoard():
	print(" " + board[1][1] + " | " + board[1][2] + " | " + board[1][3])
	print("---|---|---")
	print(" " + board[2][1] + " | " + board[2][2] + " | " + board[2][3])
	print("---|---|---")
	print(" " + board[3][1] + " | " + board[3][2] + " | " + board[3][3])


def takeTurn():
	global currentPlayer
	global currentSymbol
	global board
	global turnsTaken

	currentPlayer = players[turnsTaken%2]
	currentSymbol = symbols[turnsTaken%2]

	row = int(input(currentPlayer + ", enter the row you'd like to play (1, 2, or 3):  "))
	col = int(input(currentPlayer + ", enter the column you'd like to play (1, 2, or 3):  "))

	if ((1<=row<=3) and (1<=col<=3) and (board[row][col]=="?")): # check to see if spot isn't taken and that the move is on the board
		board[row][col] = currentSymbol
		turnsTaken += 1
	else:
		print(" *** Invalid move " + currentPlayer + "! ***")

def checkForWin():
	global gameOver
	global turnsTaken
	if board[1][1] == board[1][2] == board[1][3] == currentSymbol:
		#print("row 1")
		gameOver = True
	elif board[2][1] == board[2][2] == board[2][3] == currentSymbol:
		#print("row 2")
		gameOver = True
	elif board[3][1] == board[3][2] == board[3][3] == currentSymbol:
		#print("row 3")
		gameOver = True
	elif board[1][1] == board[2][1] == board[3][1] == currentSymbol:
		#print("col 1")
		gameOver = True
	elif board[1][2] == board[2][2] == board[3][2] == currentSymbol:
		#print("col 2")
		gameOver = True
	elif board[1][3] == board[2][3] == board[3][3] == currentSymbol:
		#print("col 3")
		gameOver = True
	elif board[1][1] == board[2][2] == board[3][3] == currentSymbol:
		print("top left to bottom right")
		gameOver = True
	elif board[3][1] == board[2][2] == board[1][3] == currentSymbol:
		#print("/")
		gameOver = True

	if gameOver:
		print(currentPlayer + " wins!")
		playAgain = input("Would you like to play again? Enter Yes or No:  ")
		if playAgain.lower() == "yes":
			resetBoard()
			printBoard()
			gameOver = False
			turnsTaken = 0
		elif playAgain.lower() == "no":
			quit()
		else:
			print("Huh? Type Yes or No.")
			checkForWin()
		
# Start Game
print(currentPlayer + ", make your move!")
resetBoard()
printBoard()
# Game Loop
while gameOver == False:
	takeTurn()
	printBoard()
	checkForWin()