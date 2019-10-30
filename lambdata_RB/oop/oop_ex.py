"""
Classes to represent games
"""
from random import random

class Game:
    """
    General representation of an abstract game
    """
    fun_level = 5

    def __init__(self,rounds=2,player1='Gayu',player2='Hiran'):
        self.rounds = rounds
        self.steps = 5
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """
        print the players for Game
        """
        print('{} Vs {} in Game'.format(self.player1,self.player2))

    def add_round(self):
        """
        increment number of rounds
        """
        self.rounds += 1

    def winner(self):
        """
        randomly pick and return winner
        """
        if (random() > 0.5):
            return self.player1
        else:
            return self.player2

# subclass TicTacToe of Game
class TTT(Game):
    """
    subclass of Game called TicTacToe
    """
    def __init__(self,rounds=3,player1='RB',player2='Sri'):
        super().__init__(rounds,player1,player2)

    def print_players(self):
        """
        print the players for TicTacToe
        """
        print('{} Vs {} in TicTacToe'.format(self.player1,self.player2))

pass
