import board
import player




def main():
    printRules()
    generatePlayers()
    
    

def printRules() -> None:
    '''Call the function to print the rules
    '''
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
    print("To move a token out of the starting area, a player must roll a 6. If a 6 is rolled, the player gets another turn.")
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
    print("The first player to get all four tokens into their home area wins the game.")

def generatePlayers()-> list:
    nameOfPlayers = input("Names of the players seperated by commas (minimum 2 and max 4)? : ").split(",")

    while(2 < len(nameOfPlayers) < 4):
        nameOfPlayers = input(" Invalid. Names of the players seperated by commas (minimum 2 and max 4)? : ").split(",")
    
    listOfPlayers = []
    for names in nameOfPlayers:
        #Pass in attributes
        listOfPlayers+= player.Player()

def printBoard() -> None:
    pass


    

    
    

    





if __name__ == "__main__":
    main()