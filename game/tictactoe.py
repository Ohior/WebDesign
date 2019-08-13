from random import choice
from copy import copy
from typing import Any

BOARD = ['']*10
player_score = 0
computer_score = 0
player_word = "X"
computer_word = "O"
smart_moves = (1,7,9,3,5)
other_moves = (2,4,8,6)
has_won = "Play TICTACTOE"
round = 1

def computerMoves(moves):
    s_moves = []
    for i in getRightMoves():
        if int(i) in moves:
            s_moves.append(int(i))
    return s_moves

def getPlayerMove():
    num = input("Enter your move number: ")
    return num

def getComputerMove(p_word, c_word):
    board_copy = copy(BOARD)
    getcom = potentialWinner(c_word,board_copy)
    if getcom:
        return str(getcom)
    getcom = potentialWinner(p_word, board_copy)
    if getcom:
        return str(getcom)
    if len(computerMoves(smart_moves)) != 0:
     return str(choice(computerMoves(smart_moves)))
    else:return  str(choice(computerMoves(other_moves)))

def potentialWinner(word, b_copy):
    for i in range(1,len(b_copy)):
        if b_copy[i].__eq__(""):
            b_copy[i]=word
            if hasWon(b_copy, word):
                return i
            else:b_copy[i] = ""
    return 0

def hasWon(bo, word):
    ways = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for w in ways:
        if bo[w[0]] == bo[w[1]] == bo[w[2]] == word:
            return True
    return False

def getRightMoves():
    rig_moves = []
    for i in range(1,10):
        if BOARD[i].__eq__(''):
            rig_moves.append(str(i))
    return rig_moves

def makeMove(bo, num, word):
    bo[num] = word

def getBoardCopy():
    bo_copy = []
    for i in BOARD:
        bo_copy.append(i)
    return bo_copy

def isRightMove(move):
    moves = getRightMoves()
    for m in moves:
        if m.__eq__(move):
            return True
    return False

def boardIsEmpty(i):
    if BOARD[i].__eq__(''):
            return True
    return False

def mainPlayer(move):
    player_word = "X"
    if isRightMove(str(move)):
        makeMove(BOARD,int(move),player_word)

def mainComputer():
    move = getComputerMove(player_word, computer_word)
    makeMove(BOARD, int(move), computer_word)

def numberOfEmptyBoard():
    num = 0
    for i in range(1,len(BOARD)):
        if boardIsEmpty(i):
            num+=1
    return num
