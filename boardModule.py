import time
from playerModule import Player

class Board:
    def __init__(self, player1:Player,player2:Player,player3:Player,player4:Player):
        '''Takes a reference of all 4 players. Whatever players name is inputed first is the first player. The boards are intialized and assigned
        as attributes of the board class.

        Parameters
        ----------
        player1 : Player
            First player
        player2 : Player
            Second player
        player3 : Player
            Third player
        player4 : Player
            Fourth player
        '''

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
            ["^","^","^","^"],
            #Player 1
            ["^","^","^","^"],
            #Player 2
            ["^","^","^","^"],
            #Player 3
            ["^","^","^","^"],
        ]
        self.homeSpace = homeSpace

        heavenSpace = [
            ["-","-","-","-","-","-"],
            ["-","-","-","-","-","-"],
            ["-","-","-","-","-","-"],
            ["-","-","-","-","-","-"]
        ]

        self.heavenSpace = heavenSpace

        spaces = {'p1': player1, 'p2':player2, 'p3': player3, 'p4': player4}
        self.spaces = spaces
    
    def getPlayerList(self) ->None:
        return (self.player1,self.player2,self.player3,self.player4)

    def setNextPlayerTurn(self)-> None:
        #Sets the next player's turn
        newPlayerIndex = self.currentPlayer.index
        
        if(newPlayerIndex == 3):
            newPlayerIndex = 0
        else:
            newPlayerIndex+=1
        
        for playah in self.getPlayerList():
            if playah.index == newPlayerIndex:
                self.currentPlayer = playah
            

    def activatePiece(self)-> None:
        for p in self.currentPlayer.getPieces():
            if not (p.actvity):
                p.activity = True
                #Each starts at their own list for their given index,t index 5 in that list
                if(self.self.mainBoard[self.currentPlayer.index][5].contains("*")):
                    self.mainBoard[self.currentPlayer.index][5] = ""

                self.mainBoard[self.currentPlayer.index][5]+=p
                break
    
    def move(self,diceRoll:int,pieceToMove:int):
        pieceToMove = self.currentPlayer.getPiece(pieceToMove)
        
                
        



        