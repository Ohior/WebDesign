from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tic/', views.tictactoe, name="tictactoe"),
    path('<str:num>', views.returnedTictactoe, name="r_tictactoe"),
    path('playagain/<again>', views.playAgainTictactoe, name="p_tictactoe"),
    path('back/', views.backTictactoe, name="back"),
]