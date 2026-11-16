#imports at the top!

#global variables
gameboard=[ [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

#functuons
def printboard(board):
    for r in range(3):
        print(f"{board[r][0]}|{board[r][1]}|{board[r][2]}")
        if r != 2:
            print("-"*5)
    print()
def userMove(symbol,board):
    print(f"It is {symbol}'s turn")
    row =int(input("row: "))-1
    col =int(input("col "))-1
    if row in range (3) and col in range(3):
        if gameboard[row][col] == " ":
            gameboard[row][col]=symbol



printboard(gameboard)
#Mainloop
player = "X" 
while(player !="Q"):
#Draw board
    printboard(gameboard)
#user makes a turn
    userMove("x",gameboard)
    if player == "X":
        player="O"
    else:
        player="X"
#Check for a winner or a cat
#   vertical
#   horizontal
#   diagonal
#   
#   checkForCAT
#


print("Good Game Mate!")


















