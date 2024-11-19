
class Pieces():

    def __init__(self,pos:str,player:str,activity:bool):
        #if a piece is in its players territory, and is on the 6 sixth square it becomes inactive and enters home state.
    
        self.position = pos
        self.isActive = activity
        self.player = player

    
