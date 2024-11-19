import time
import random
from player import Player

class board:
    def __init__(self,firstTurnPlayer:Player,player1:Player,player2:Player,player3:Player = None,player4:Player = None):
        self.player1 = player1
        self.player2 = player2

        if not player3 == None:
            self.player3 = player3
        if not player4 == None:
            self.player4 = player4
        
        self.currentPlayer = firstTurnPlayer

        #A board to represent the game. Indexes represent whose territory it is, so 0 is firstPlayer, 1 is secondPlayer
        #First index of each list corresponds to the top right of the territory. Index 6 is special becase it is the first
        #chance to make it to home.
        board = [
            #0,   1   2   3   4   5   6   7   8   9   10  11  12 
            [" "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        ]

    def rollDice() -> int:
        return random.randint(1,6)
        