from boardModule import Board
from random import randint


NUMHEAVENSPACES = 58

def main():
    printRules()

    #Generate the players as tuple and return that to be assigned to the board
    #generatePlayers()

    #Pass in the players as parameters
    ludoBoard = Board()

    #for loop to iterate through the game
    
    

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
    pass
   #generate on 4 players

def printBoard(boardP:Board) -> None:
    #boardP.mainBoard -> this is a reference to the main board pieces (the one that all pieces share)
    #boardP.homeSpace
    #boardP.heavenSpace
    print(f'      {boardP.mainBoard[0][7]}{boardP.mainBoard[0][6]}{boardP.mainBoard[0][5]}      ')
    print(f'   {boardP.homeSpace[1][0]}  {boardP.mainBoard[0][8]}{boardP.heavenSpace[0][0]}{boardP.mainBoard[0][4]}  {boardP.homeSpace[0][0]}   ')
    print(f'  {boardP.homeSpace[1][1]} {boardP.homeSpace[1][2]} {boardP.mainBoard[0][9]}{boardP.heavenSpace[0][1]}{boardP.mainBoard[0][3]} {boardP.homeSpace[0][1]} {boardP.homeSpace[0][2]}  ')
    print(f'   {boardP.homeSpace[1][3]}  {boardP.mainBoard[0][10]}{boardP.heavenSpace[0][2]}{boardP.mainBoard[0][2]}  {boardP.homeSpace[0][3]}   ')
    print(f'      {boardP.mainBoard[0][11]}{boardP.heavenSpace[0][4]}{boardP.mainBoard[0][1]}      ')
    print(f'      {boardP.mainBoard[0][12]}{boardP.mainBoard}')
    print(boardP.mainBoard[0][2])

    print(f'  {boardP.homeSpace[2][1]} {boardP.homeSpace[2][2]} {boardP.mainBoard[2][3]}{boardP.heavenSpace[2][1]}{boardP.mainBoard[2][9]} {boardP.homeSpace[3][1]} {boardP.homeSpace[3][2]}')
    print(f'   {boardP.homeSpace[2][3]}  {boardP.mainBoard[2][4]}{boardP.heavenSpace[2][0]}{boardP.mainBoard[2][8]}  {boardP.homeSpace[3][3]}   ')
    print(f'      {boardP.mainBoard[2][5]}{boardP.mainBoard[2][6]}{boardP.mainBoard[2][7]}      ')


def rollDice() -> int:
        return randint(1,6)
    


    
if __name__ == "__main__":
    main()