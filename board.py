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

        #A board to represent the game.

    def rollDice() -> int:
        return random.randint(1,6)
        