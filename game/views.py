from django.shortcuts import render, redirect
from . import tictactoe as tic
from .models import Website


def index(request):
    website = Website.objects.get()
    context = dict(website=website, tic=tic)
    return render(request, 'game/index.html', context)


def tictactoe(request):
    website = Website.objects.get()
    context = dict(website=website, tic=tic)
    return render(request, 'game/tictactoe.html', context)

def returnedTictactoe(request, num):
    if tic.numberOfEmptyBoard() > 1:
        if not tic.hasWon(tic.BOARD, tic.computer_word) and not tic.hasWon(tic.BOARD, tic.player_word):
            tic.mainPlayer(num)
            if tic.hasWon(tic.BOARD,tic.player_word):
                tic.has_won = "player won"
                tic.player_score+=1
        if not tic.hasWon(tic.BOARD, tic.player_word) and not tic.hasWon(tic.BOARD, tic.computer_word):
            tic.mainComputer()
            if tic.hasWon(tic.BOARD,tic.computer_word):
                tic.has_won = "computer won"
                tic.computer_score+=1
    return redirect("tictactoe")

def playAgainTictactoe(request, again):
    if int(again) == 0 and tic.numberOfEmptyBoard() < 9:
        tic.round += 1
        tic.BOARD = [""]*10
        tic.has_won = "Round {}".format(tic.round)
    return redirect("tictactoe")

def backTictactoe(request):
    tic.has_won = "TICTACTOE"
    tic.BOARD = [""]*10
    tic.player_score = 0
    tic.computer_score = 0
    tic.round = 1
    return redirect("index")
