

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
        self.piece1 = Pieces(name,1)
        self.piece2 = Pieces(name,2)
        self.piece3 = Pieces(name,3)
        self.piece4 = Pieces(name,4)

        self.score = 0


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
        self.isActive = False

        #Stores which player the piece belongs to.
        self.player = player

        #Stores what number piece it is.
        self.number = number