import time
from playerModule import Player

class Board:
    def __init__(self, player1:Player,player2:Player,player3:Player,player4:Player):

        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        
        self.currentPlayer = player1

        #A board to represent the game. Indexes represent whose territory it is, so 0 is firstPlayer, 1 is secondPlayer,etc.
        #* represents an empty space on the board
        mainBoard = [
            #0,   1   2   3   4   5   6   7   8   9   10  11  12 
            ["*","*","*","*","*","*","*","*","*","*","*","*","*"],
            ["*","*","*","*","*","*","*","*","*","*","*","*","*"],
            ["*","*","*","*","*","*","*","*","*","*","*","*","*"],
            ["*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ]
        self.mainBoard = mainBoard

        
        homeSpace = [
            #Player 0
            ["","","",""],
            #Player 1
            ["","","",""],
            #Player 2
            ["","","",""],
            #Player 3
            ["","","",""],
        ]
        self.homeSpace = homeSpace

        heavenSpace = [
            ["*","*","*","*","*","*"],
            ["*","*","*","*","*","*"],
            ["*","*","*","*","*","*"],
            ["*","*","*","*","*","*"],
        ]

        self.heavenSpace = heavenSpace


    
        