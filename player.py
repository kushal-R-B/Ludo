import pieces

class Player():

    def __init__(self,name:str):
        #Write player attributes 
        self.name = name
        
        #Intialize all the pieces:
        self.piece1 = pieces.Pieces(name)