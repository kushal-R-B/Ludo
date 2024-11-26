
from random import randint

NUMTOHEAVENSPACES = 52

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
    # dictionary to keep track of player scores
    player_score = {
        player1.name: player1.score,
        player2.name: player2.score,
        player3.name: player3.score,
        player4.name: player4.score
    }
    #for loop to iterate through the game
    userInput = ""

    while True:
        currentPlayer = ludoBoard.currentPlayer
        piecesTup = currentPlayer.getPieces()
        
        print(f"{currentPlayer.name}'s turn!")
        diceRoll = rollDice()
        
        print(f"The dice landed on {diceRoll}")
        
        if currentPlayer.score < 4:
            if (not currentPlayer.isAllPiecesActive() and (diceRoll == 1 or diceRoll == 6)):
                print("Would you like to activate a piece?")
                userInput = input("Y/N: ")

                if userInput.lower() == "stop":
                    break
                
                # Activate a piece
                if userInput.lower() == "y":
                    ludoBoard.activatePiece()
                # If they don't want to activate a piece, then ask them to move a piece from their active ones
                else:
                    activePieces = currentPlayer.getActivePieces()
                    for p in activePieces:
                        print(f"Piece {p.number}: ")
                    # Takes the piece that you want to move
                    userInput = input("What piece would you like to move?: ")
                    if userInput.lower() == "stop":
                        break
                    # Now ask the board to move
                    ludoBoard.move(diceRoll, int(userInput))
            else:
                if currentPlayer.piecesActivated > 0:
                    activePieces = currentPlayer.getActivePieces()
                    for p in activePieces:
                        print(f"Piece {p.number}")
                    # Takes the piece that you want to move
                    userInput = input("What piece would you like to move?: ")
                    if userInput.lower() == "stop":
                        break
                    # Now ask the board to move
                    ludoBoard.move(diceRoll, int(userInput))
                else:
                    print("No pieces to move. Rolling again.")
                    ludoBoard.setNextPlayerTurn()
                #    continue

        # Ensure the turn switches to the next player
        ludoBoard.setNextPlayerTurn()
        printBoard(ludoBoard)

        if userInput.lower() == "stop":
            break


    


    #Iterate through all players and add them
    print("Game Over!, Check final_score.txt")
    player_score[currentPlayer.name] = currentPlayer.score
    writefinalscore([player1,player2,player3,player4])
        
            

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
        invalid_symbols = "*^-"
        for name in [name1, name2, name3, name4]:
            if any(symbol in name for symbol in invalid_symbols):
                raise ValueError("Name cannot contain the symbols *, ^, or -.")
    except ValueError:
            print("Inalid Inputs for Character Inputs. Game Ending...")
            exit()

    return (Player(name1,0,0),Player(name2,1,13),Player(name3,2,26),Player(name4,3,39))


def printBoard(boardP: 'Board') -> None:
    '''Maps out the drawing of the board with the spaces that the players can land on

    Parameters
    ----------
    boardP : Board
        Takes in the board with the spaces that it belongs with
    '''
    print(f'      {boardP.mainBoard[24]}{boardP.mainBoard[25]}{boardP.mainBoard[26]}      ')
    print(f'   {boardP.homeSpace[1][0]}  {boardP.mainBoard[23]}{boardP.heavenSpace[0][0]}{boardP.mainBoard[27]}  {boardP.homeSpace[0][0]}   ')
    print(f'  {boardP.homeSpace[1][1]} {boardP.homeSpace[1][2]} {boardP.mainBoard[22]}{boardP.heavenSpace[0][1]}{boardP.mainBoard[28]} {boardP.homeSpace[0][1]} {boardP.homeSpace[0][2]}  ')
    print(f'   {boardP.homeSpace[1][3]}  {boardP.mainBoard[21]}{boardP.heavenSpace[0][2]}{boardP.mainBoard[29]}  {boardP.homeSpace[0][3]}   ')
    print(f'      {boardP.mainBoard[20]}{boardP.heavenSpace[0][3]}{boardP.mainBoard[30]}      ')
    print(f'      {boardP.mainBoard[19]}{boardP.heavenSpace[0][4]}{boardP.mainBoard[31]}      ')
    print(f'{boardP.mainBoard[13]}{boardP.mainBoard[14]}{boardP.mainBoard[15]}{boardP.mainBoard[16]}{boardP.mainBoard[17]}{boardP.mainBoard[18]} {boardP.heavenSpace[0][5]} {boardP.mainBoard[32]}{boardP.mainBoard[33]}{boardP.mainBoard[34]}{boardP.mainBoard[35]}{boardP.mainBoard[36]}{boardP.mainBoard[37]}')
    print(f'{boardP.mainBoard[12]}{boardP.heavenSpace[1][0]}{boardP.heavenSpace[1][1]}{boardP.heavenSpace[1][2]}{boardP.heavenSpace[1][3]}{boardP.heavenSpace[1][4]}{boardP.heavenSpace[1][5]} {boardP.heavenSpace[3][5]}{boardP.heavenSpace[3][4]}{boardP.heavenSpace[3][3]}{boardP.heavenSpace[3][2]}{boardP.heavenSpace[3][1]}{boardP.heavenSpace[3][0]}{boardP.mainBoard[38]}')
    print(f'{boardP.mainBoard[11]}{boardP.mainBoard[10]}{boardP.mainBoard[9]}{boardP.mainBoard[8]}{boardP.mainBoard[7]}{boardP.mainBoard[6]} {boardP.heavenSpace[2][5]} {boardP.mainBoard[44]}{boardP.mainBoard[43]}{boardP.mainBoard[42]}{boardP.mainBoard[41]}{boardP.mainBoard[40]}{boardP.mainBoard[39]}')
    print(f'      {boardP.mainBoard[5]}{boardP.heavenSpace[2][4]}{boardP.mainBoard[45]}')
    print(f'      {boardP.mainBoard[4]}{boardP.heavenSpace[2][3]}{boardP.mainBoard[46]}      ')
    print(f'   {boardP.homeSpace[2][0]}  {boardP.mainBoard[3]}{boardP.heavenSpace[2][2]}{boardP.mainBoard[47]}  {boardP.homeSpace[3][0]}   ')
    print(f'  {boardP.homeSpace[2][1]} {boardP.homeSpace[2][2]} {boardP.mainBoard[2]}{boardP.heavenSpace[2][1]}{boardP.mainBoard[48]} {boardP.homeSpace[3][1]} {boardP.homeSpace[3][2]}')
    print(f'   {boardP.homeSpace[2][3]}  {boardP.mainBoard[1]}{boardP.heavenSpace[2][0]}{boardP.mainBoard[49]}  {boardP.homeSpace[3][3]}   ')
    print(f'      {boardP.mainBoard[0]}{boardP.mainBoard[51]}{boardP.mainBoard[50]}      ')



    

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
    def __init__(self, player1: 'Player', player2: 'Player', player3: 'Player', player4: 'Player'):
        '''Takes a reference of all 4 players. Whatever players name is inputed first is the first player. The boards are initialized and assigned
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

        # A board to represent the game. Indexes represent whose territory it is, so 0 is firstPlayer, 1 is secondPlayer, etc.
        # * represents an empty space on the board

        # Manually initialize the mainBoard list with 52 elements
        self.mainBoard = [
            "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
            "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
            "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
            "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
            "*", "*", "*", "*"
        ]

        # Example initialization for homeSpace and heavenSpace
        self.homeSpace = [["^"] * 4 for _ in range(4)]
        self.heavenSpace = [["-"] * 6 for _ in range(4)]


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
        '''Activates a  single piece by using the reference of currentPlayer
        '''
        for p in self.currentPlayer.getPieces():
            if not (p.activity):
                p.activity = True
                self.currentPlayer.piecesActivated+=1
                #Each starts at their own list for their given index,t index 5 in that list
                if("*" in self.mainBoard[self.currentPlayer.startIndex]):
                    self.mainBoard[self.currentPlayer.startIndex] = self.currentPlayer.symbol
                else:
                    self.mainBoard[self.currentPlayer.index] += self.currentPlayer.symbol
                    
                break
    
    def move(self, diceRoll: int, numberPieceToMove: int):
        curPiece = self.currentPlayer.getPiece(numberPieceToMove)
        curPlayersPiece = self.currentPlayer.getPieces()

        for i in range(diceRoll):
            curPiece.stepCount += 1

            # Check if the piece should move to heaven
            if curPiece.stepCount >= NUMTOHEAVENSPACES and not curPiece.isInHeaven:
                self.heavenSpace[self.currentPlayer.index][0] = self.currentPlayer.symbol
                curPiece.isInHeaven = True
                curPiece.stepCount = 0  # Reset step count for heaven

            # Determine the next position on the main board
            nextPosition = curPiece.indexInMainBoard + 1

            # Handle wrapping around the board
            if nextPosition >= len(self.mainBoard):
                nextPosition -= len(self.mainBoard)

            charactersAhead = self.mainBoard[nextPosition]

            # Move the piece one step on the board visually
            if self.currentPlayer.symbol in charactersAhead:
                self.mainBoard[nextPosition] += self.currentPlayer.symbol
            else:
                self.mainBoard[nextPosition] = self.currentPlayer.symbol

            # Handle the removal of other pieces
            if "*" not in charactersAhead and not curPiece.isInHeaven and self.currentPlayer.symbol not in charactersAhead:
                temp = self.getPlayerList()
                tempPlayer = None
                for playah in temp:
                    if playah.symbol in charactersAhead:
                        tempPlayer = playah
                        break

                playahsPieces = tempPlayer.getPieces()
                for p in playahsPieces:
                    if p.indexInMainBoard == nextPosition:
                        p.indexInMainBoard = tempPlayer.startIndex
                        p.stepCount = 0
                        p.activity = False

            # Update the current piece's location
            curPiece.indexInMainBoard = nextPosition

            # Update the previous position to be empty
            if curPiece.indexInMainBoard - 1 >= 0:
                self.mainBoard[curPiece.indexInMainBoard - 1] = "*"

        # Check if the piece has scored
        if curPiece.isInHeaven and curPiece.stepCount % 6 == 0:
            self.currentPlayer.score += 1
            self.currentPlayer.pieces.remove(curPiece)
            del curPiece

                

#playerModule--------------------------------------------------------------------------------------------------------------------------------------
class Player():
    def __init__(self,name:str,index:int,startIndex:int):
        '''Intializes the object of Player Class with the name of the player
        the index corresponding to the list of that player's territory within the matrix,
        the player's pieces, and the score (number of pieces in heaven)

        Parameters
        ----------
        name : str
            Name of the player.
        index : int
            An integer describing what the int of the heaven list the pieces of that player should go to.
        startIndex: int
            An integer that descibes the index that the piece should be sent if activated.
        
        Attributes
        ----------
        pieces: Pieces
            object from Pieces class in pieceModule, assigned with attibute numbers 0 to 3
        score: int
            Stores the number of pieces that have reached the step
            count
        piecesActivated: int
            Stores the number of pieces activated
        index : int
            An integer describing what the int of the heaven list the pieces of that player should go to.
        startIndex: int
            An integer that descibes the index that the piece should be sent if activated.

        '''
        #Symbol
        self.symbol = name[0]

        #Assings the terriorty number, an integer from 0 to 3 which assigns their heavens
        self.index = index
    
        #Player names
        self.name = name
        
        #Intialize all the pieces from 1 to 4:
        self.piece1 = Pieces(self,1,startIndex)
        self.piece2 = Pieces(self,2,startIndex)
        self.piece3 = Pieces(self,3,startIndex)
        self.piece4 = Pieces(self,4,startIndex)

        #Numbe of pieces scored
        self.score = 0

        #Start index
        self.startIndex = startIndex

        #Number of piecesActivated
        self.piecesActivated = 0
    
    def score_piece(self, piece) ->None: 
        '''Deletes a piece once it scores.

        Parameters
        ----------
        piece : Pieces
            Pass in the piece to delete.
        '''
        self.pieces.remove(piece) 
        del piece

    def getPieces(self) -> list:
        '''Returns a tuple with the players current pieces

        Returns
        -------
        list
            A list consisting of all the player's pieces, checks if the piece has been deleted before
            adding to return list.
        '''
        temp = []

        if not self.piece1 == None:
            temp+=[self.piece1]
        if not self.piece2 == None:
            temp+=[self.piece2]
        if not (self.piece3 == None):
            temp+=[self.piece3]
        if not self.piece4 == None :
            temp+=[self.piece4]
        
        return temp
    
    def getActivePieces(self) -> list:
        temp = self.getPieces()
        temp2 = []
        for p in temp:
            if p.activity == True:
                temp2+= [p]
        
        return temp2

    
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
        '''Returns if all the player's pieces are active

        Returns
        -------
        bool
            Returns true if all the players pieces are activated.
        '''
        temp = self.getPieces()
        for p in temp:
            if p.activity == False:
                return False

        return True
        


class Pieces():

    def __init__(self,player:Player,number:int,indexInMainBoard:int):
        '''A piece on the board, that is attribute of each player. 

        Parameters
        ----------
        player : Player
            Takes in the reference of the player that the piece belongs to.
        activity: bool
            Sets the acitivity of the piece. Piece is activated by the board
        number: int
            Take in the number in the heaven matrix that the player owns
        indexInMainBoard: int
            Takes in the starting index for each player. Updated in the moved method.
        
        Attributes
        ----------
        player : Player
            Takes in the reference of the player that the piece belongs to.
        activity: bool
            Sets the acitivity of the piece. Piece is activated by the board
        number: int
            Take in the number in the heaven matrix that the player owns
        indexInMainBoard: int
            Takes in the starting index for each player. Updated in the moved method.
        isInHeaven: bool
            Boolean value that tells wheter the piece is in heaven or not.
        
       
        '''
        # Holds the number of steps that the piece, has, 
        # it has to match a certain amount to reach heaven and score
        self.stepCount = 0 

        #Stores whether the piece is active or not 
        #(you need to roll a specific number to activate a piece)
        self.activity = False

        #Stores which player the piece belongs to.
        self.player = player

        #Stores what number piece it is.
        self.number = number

        #Stores the location, so it starts a the players index, with the assigned number of the piece being 
        self.indexInMainBoard = indexInMainBoard

        self.isInHeaven = False
         
    
    def activatePiece(self) -> None: 
        '''Changes the activity of the piece to true.''' 
        self.activity = True
        
    
        # apend to document player # has # piece in heaven

def writefinalscore(players):
    ''' writes the final score in a new file'''
    with open("final_score.txt", "w") as file:
        for player in players:
            file.write(f"{player.name}: {player.score}\n") 
        
                
if __name__ == "__main__":
    main()