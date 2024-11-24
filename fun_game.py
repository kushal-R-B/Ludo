
from random import randint

NUMTOHEAVENSPACES = 58

def main():
    '''Ran as the main script of the program.
    '''
    #Print the rules
    printRules()

    #prints the game commands
    printCommands()

    #Generate the players as tuple and return that to be assigned to the board
    player1, player2, player3,player4 = generatePlayers()
    #Pass in the players as parameters
    ludoBoard = Board(player1,player2,player3,player4)
   
    #for loop to iterate through the game
    userInput = ""

    while(not(userInput =="stop")):
        currentPlayer = ludoBoard.currentPlayer
        piecesTup = currentPlayer.getPieces()
        
        print(f"{currentPlayer.name}'s turn!")
        diceRoll = rollDice()
    
        print(f"The dice landed on {diceRoll}")
        
        if(not(currentPlayer.isAllPiecesActive()) and (diceRoll == 1 or diceRoll == 6) ):
            print("Would you like to activate a piece?")
            userInput = input("Y/N: ")
            
            #Activate a piece
            if(userInput == "Y"):
                ludoBoard.activatePiece()
            #If they don't want to activate a piece, then ask them to move a piece.
            else:
                pass
        #All the pieces they have been activated, then don't ask them to activate and instead move on to move.
        elif(currentPlayer.piecesActivated > 0):
            input("What piece would you like to move?")
            for p in piecesTup:
                if(p.activity == True):
                    print(f"{p.number}")
        
        
        ludoBoard.setNextPlayerTurn()
        printBoard(ludoBoard)
            

def printRules() -> None:
    '''Call the function to print the rules'''
    print("===================================")
    print("          LUDO GAME RULES          ")
    print("===================================")
    print("\nGoal:")
    print("The objective of the game is to be the first player to get all four of your tokens from your starting area to your home area.")
    print("\nSetup:")
    print("Each player chooses a color and takes four tokens of that color.")
    print("Place your tokens in your starting area.")
    print("Decide the order of play by rolling the dice. The highest roller goes first.")
    print("\nBasic Rules:")
    print("Starting the Game:")
    print("Players take turns rolling a single die.")
    print("To move a token out of the starting area, a player must roll a 1 or a 6. If either is rolled, the player gets another turn.")
    print("\nMoving Tokens:")
    print("Move your tokens according to the number rolled on the die.")
    print("If you roll a 6, you get an additional turn.")
    print("Tokens move clockwise around the board along the path of their color.")
    print("\nCapturing Tokens:")
    print("If a token lands on a space occupied by an opponent's token, the opponent's token is sent back to their starting area.")
    print("A token cannot land on a space occupied by another token of the same color.")
    print("\nSafe Zones:")
    print("Each color has a safe zone near the home area where tokens cannot be captured by opponents.")
    print("Tokens must enter the safe zone by exact count.")
    print("\nEntering Home:")
    print("Tokens must enter the home area by exact count.")
    print("The first player to get all four tokens into their home area wins the game.\n\n")

def printCommands():
    print()
    print("===================================")
    print("         LUDO GAME Commands        ")
    print("===================================")
    print("-STOP to end game.")
    print("-SCORE to check score")

    print("\n\n")
    
    

def generatePlayers()-> tuple:
    '''Creates instances of players, with the name and index number passed in as parameters.
    Returns
    -------
    tuple
        Generates a tuple with a reference to each player
    '''
    print("Enter the names of player.")
    try:
        name1 = input("Enter Name for Player 1: ")
        name2 = input("Enter Name for Player 2: ")
        name3 =input("Enter Name for Player 3: ")
        name4 = input("Enter Name for Player 4: ")
    except:
        if(name1 in "*^-" or name2 in "*^-" or name3 in "*^-" or name4 in "*^-"):
            print('Name can not be the same symbol as the board.')

    return (Player(name1,0),Player(name2,1),Player(name3,2),Player(name4,3))


def printBoard(boardP:'Board') -> None:
    '''Maps out the drawing of the board with the spaces that the players can land on

    Parameters
    ----------
    boardP : Board
        Takes in the board with the spaces that it belongs with
    '''
    print(f'      {boardP.mainBoard[0][7]}{boardP.mainBoard[0][6]}{boardP.mainBoard[0][5]}      ')
    print(f'   {boardP.homeSpace[1][0]}  {boardP.mainBoard[0][8]}{boardP.heavenSpace[0][0]}{boardP.mainBoard[0][4]}  {boardP.homeSpace[0][0]}   ')
    print(f'  {boardP.homeSpace[1][1]} {boardP.homeSpace[1][2]} {boardP.mainBoard[0][9]}{boardP.heavenSpace[0][1]}{boardP.mainBoard[0][3]} {boardP.homeSpace[0][1]} {boardP.homeSpace[0][2]}  ')
    print(f'   {boardP.homeSpace[1][3]}  {boardP.mainBoard[0][10]}{boardP.heavenSpace[0][2]}{boardP.mainBoard[0][2]}  {boardP.homeSpace[0][3]}   ')
    print(f'      {boardP.mainBoard[0][11]}{boardP.heavenSpace[0][4]}{boardP.mainBoard[0][1]}      ')
    print(f'      {boardP.mainBoard[0][12]}{boardP.heavenSpace[0][4]}{boardP.mainBoard[0][0]}      ')
    print(f'{boardP.mainBoard[1][5]}{boardP.mainBoard[1][4]}{boardP.mainBoard[1][3]}{boardP.mainBoard[1][2]}{boardP.mainBoard[1][1]}{boardP.mainBoard[1][0]} {boardP.heavenSpace[0][5]} {boardP.mainBoard[3][12]}{boardP.mainBoard[3][11]}{boardP.mainBoard[3][10]}{boardP.mainBoard[3][9]}{boardP.mainBoard[3][8]}{boardP.mainBoard[3][7]}')
    print(f'{boardP.mainBoard[1][6]}{boardP.heavenSpace[1][0]}{boardP.heavenSpace[1][1]}{boardP.heavenSpace[1][2]}{boardP.heavenSpace[1][3]}{boardP.heavenSpace[1][4]}{boardP.heavenSpace[1][5]} {boardP.heavenSpace[3][5]}{boardP.heavenSpace[3][4]}{boardP.heavenSpace[3][3]}{boardP.heavenSpace[3][2]}{boardP.heavenSpace[3][1]}{boardP.heavenSpace[3][0]}{boardP.mainBoard[3][6]}')
    print(f'{boardP.mainBoard[1][7]}{boardP.mainBoard[1][8]}{boardP.mainBoard[1][9]}{boardP.mainBoard[1][10]}{boardP.mainBoard[1][11]}{boardP.mainBoard[1][12]} {boardP.heavenSpace[2][5]} {boardP.mainBoard[3][0]}{boardP.mainBoard[3][1]}{boardP.mainBoard[3][2]}{boardP.mainBoard[3][3]}{boardP.mainBoard[3][4]}{boardP.mainBoard[3][5]}')
    print(f'      {boardP.mainBoard[2][0]}{boardP.heavenSpace[2][4]}{boardP.mainBoard[2][12]}')
    print(f'      {boardP.mainBoard[2][1]}{boardP.heavenSpace[2][3]}{boardP.mainBoard[2][11]}      ')
    print(f'   {boardP.homeSpace[2][0]}  {boardP.mainBoard[2][2]}{boardP.heavenSpace[2][2]}{boardP.mainBoard[2][10]}  {boardP.homeSpace[3][0]}   ')
    print(f'  {boardP.homeSpace[2][1]} {boardP.homeSpace[2][2]} {boardP.mainBoard[2][3]}{boardP.heavenSpace[2][1]}{boardP.mainBoard[2][9]} {boardP.homeSpace[3][1]} {boardP.homeSpace[3][2]}')
    print(f'   {boardP.homeSpace[2][3]}  {boardP.mainBoard[2][4]}{boardP.heavenSpace[2][0]}{boardP.mainBoard[2][8]}  {boardP.homeSpace[3][3]}   ')
    print(f'      {boardP.mainBoard[2][5]}{boardP.mainBoard[2][6]}{boardP.mainBoard[2][7]}      ')


def rollDice() -> int:
    '''_summary_

    Returns
    -------
    int
        _description_
    '''
    return randint(1,6)
    
    

#boardModule--------------------------------------------------------------------------------------------------------------------------------
class Board:
    def __init__(self, player1:'Player',player2:'Player',player3:'Player',player4:'Player'):
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
    
    def getPlayerList(self) ->tuple:
        '''Returns a tuple of the players on the board

        Returns
        -------
        tuple
            Consists of all the players in the game
        '''

        return (self.player1,self.player2,self.player3,self.player4)

    def setNextPlayerTurn(self)-> None:
        '''Finds the new player index by incrementing by one are restarting to zero. Then finds the player with that
        index and sets as the current player.'''
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
        '''Activates a piece by using the reference of currentPlayer
        '''
        for p in self.currentPlayer.getPieces():
            if not (p.activity):
                p.activity = True
                #Each starts at their own list for their given index,t index 5 in that list
                if("*" in self.mainBoard[self.currentPlayer.index][5]):
                    self.mainBoard[self.currentPlayer.index][5] = ""

                self.mainBoard[self.currentPlayer.index][5] += self.currentPlayer.symbol
                break
    
    def move(self,diceRoll:int,pieceToMove:int):
        pieceMove = self.currentPlayer.getPiece(pieceToMove)
        location = pieceMove.location.split("-") #splits on the - so that it can idenitfy which board,
        print("Hello")


#playerModule--------------------------------------------------------------------------------------------------------------------------------------
class Player():
    def __init__(self,name:str,index:int):
        '''Intializes the object of Player Class with the name of the player
        the index corresponding to the list of that player's territory within the matrix,
        the player's pieces, and the score (number of pieces in heaven)

        Parameters
        ----------
        name : str
            Name of the player.
        index : int
            An integer describing what the int of the list is.
        
        Attributes
        ----------
        pieces: Pieces
            object from Pieces class in pieceModule, assigned with attibute numbers 0 to 3
        score: int
            Stores the number of pieces that have reached the step
            count
        piecesActivated: int
            Stores the number of pieces activated

        '''
        #Symbol
        self.symbol = name[0]

        #Assings the terriorty number, an integer from 0 to 3
        self.index = index
    
        #Player names
        self.name = name
        
        #Intialize all the pieces from 0 to 3:
        self.piece1 = Pieces(self,0)
        self.piece2 = Pieces(self,1)
        self.piece3 = Pieces(self,2)
        self.piece4 = Pieces(self,3)

        self.score = 0

        self.piecesActivated = 0
    def getPieces(self) -> tuple:
        '''Returns a tuple with the players current pieces

        Returns
        -------
        tuple
            A tuple consisting of all the player's pieces.
        '''
        return self.piece1, self.piece2, self.piece3, self.piece4
    
    def getPiece(self,num:int) -> 'Pieces':
        '''Gets a piece based off the number input.

        Parameters
        ----------
        num : int
            Number corresponding to the number of the piece when it is intialized.

        Returns
        -------
        Pieces
            Finds the piece from the player attributes that corresponds to the correct number.
        '''
        piecesTuple = self.getPieces()

        for p in piecesTuple:
            if p.number == num:
                return p
    
            
    
    def isAllPiecesActive(self) -> bool:
        '''Returns if the player's pieces are activated yet.

        Returns
        -------
        bool
            Returns true if all the players pieces are activated.
        '''

        if(self.piece1.activity and self.piece2.activity and self.piece3.activity and self.piece4.activity):
            return True
        else:
            return False


class Pieces():

    def __init__(self,player:Player,number:int):
        '''A piece on the board, that is attribute of each player. 

        Parameters
        ----------
        player : Player
            Takes in the reference of the player that the piece belongs to.
       
        '''
        # Holds the number of steps that the piece, has, 
        # it has to match a certain amount to reach heaven and score
        self.stepCount = 0 

        #Stores whether the piece is active or not 
        #(you need to roll a specific number to activate a piece)
        self.activity = False

        #Stores which player the piece belongs to.
        self.player = player

        #Stores Location

        #Stores what number piece it is.
        self.number = number

        #Stores the location, so it starts a the players home index, with the assigned number of the piece being 
        # its index piece
        self.location = f"Home-{player.index}-{number}"
        

    
    # Define a custom print by calling the self.player
    def __str__(self): 
        return f"{self.player.symbol}" 
    
    def activatePiece(self) -> None: 
        '''Changes the activity of the piece to true.''' 
        self.activity = True
        
    
        # apend to document player # has # piece in heaven

# def writeLog():
#     '''Collects the data about the player and adds to file called game_log'''
#     open('game_log.txt', 'w')
#     if()
        
                


if __name__ == "__main__":
    main()