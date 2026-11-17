#import at the very top

#global variable
gameboard=[[" "," "," "],
           [" "," "," "],
           [" "," "," "]
        ]

#functions
def printboard(board):
    for r in range(3):
        print(f"{board[r][0]}|{board[r][1]}|{board[r][2]}")
        if r != 2:
            print("-"*5)
    print()

def userMove(symbol,board):
    print(f"It is {symbol}'s turn")
    row =int(input("row: "))-1    
    col =int(input("col: "))-1
    #in range
    validSpot=False
    while(not validSpot):
        if (row in range(3) and col in range(3)):
            if board[row][col] == " ":
                validSpot=True
                break
            print("Seat Taken",end=" - ")
        print("Invalid Spot")
        row =int(input("row: "))-1    
        col =int(input("col: "))-1    
    board[row][col]=symbol
   

def checkForCAT(board):
    for eachRow in board:
        for eachSpot in eachRow:
            if eachSpot == " ":
                return False
    print("CAT GAME")
    return True



def checkForWinner(p,gameboard):
    return False
#   vertical
#   horizontal
    for r in board:
        if r[0] == r[1] and r[1] == r[2] and r[0] != " ":
            print("Winner Winner Turkey Dinner!!")
            print(f"{p}")
            return True
#   diagonal
if board[0][0] == board[1][1] and board[2][2] and board[0][0] != " ":
    print("Winner Winner Turkey Dinner!!")
    print(f"{p} won!")
    return True
return False


#mainloop
player = "X"
while(player!="Q"):
    #Draw board
    printboard(gameboard)
    #user makes a turn
    userMove(player,gameboard)
    #check for winner or cat
    if checkForCAT(gameboard) or checkForWinner(player,gameboard):
        break
    #swap turns
    if player == "X":
        player="O"
    else:
        player="X"


print("\n"*10)
printboard(gameboard)
print("Good Game Mate")
