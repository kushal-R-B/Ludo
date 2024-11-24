

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
            object from Pieces class in pieceModule
        score: int
            Stores the number of pieces that have reached the step
            count
        '''
        #Symbol
        self.symbol = name[0]

        #Assings the terriorty number, an integer from 0 to 3
        self.index = index
    
        #Player names
        self.name = name
        
        #Intialize all the pieces:
        self.piece1 = Pieces(name,0)
        self.piece2 = Pieces(name,1)
        self.piece3 = Pieces(name,2)
        self.piece4 = Pieces(name,3)

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
        

        #Stores what number piece it is.
        self.number = number

        #Stores the location, so it starts a the players home index, with the assigned number
        self.location = f"Home-{player.index}-{number}"


        #Define a custom print for a piece object.
    def __str__(self):
        return f"{self.player.symbol}"
        
    def activatePiece(self) -> None:
        self.activity = True

