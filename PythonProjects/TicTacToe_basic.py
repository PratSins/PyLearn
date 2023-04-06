
def sum(a,b,c):
    return a+b+c

def printBoard(xState, zState):
    zero =   'X' if xState[0] else ('O' if zState[0] else 0)
    one =    'X' if xState[1] else ('O' if zState[1] else 1)
    two =    'X' if xState[2] else ('O' if zState[2] else 2)
    three =  'X' if xState[3] else ('O' if zState[3] else 3)
    four =   'X' if xState[4] else ('O' if zState[4] else 4)
    five =   'X' if xState[5] else ('O' if zState[5] else 5)
    six =    'X' if xState[6] else ('O' if zState[6] else 6)
    seven =  'X' if xState[7] else ('O' if zState[7] else 7)
    eight =  'X' if xState[8] else ('O' if zState[8] else 8)
    
    print (f"{zero} | {one} | {two} ")
    print (f"--|---|--")
    print (f"{three} | {four} | {five} ")
    print (f"--|---|---")
    print (f"{six} | {seven} | {eight}") 

def checkWin(xState, zState):
    wins = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum( xState[win[0]],xState[win[1]],xState[win[2]] ) == 3):
            print("\nX won the match\n")
            printBoard(xState, zState)
            return 1
        if(sum( zState[win[0]],zState[win[1]],zState[win[2]] ) == 3):
            print("\nO won the match\n")
            printBoard(xState, zState)
            return 0
    return -1

def drawState(xState, zState):
    c = 0
    for i in xState:
        if(i==1):
            c+=1
    for i in zState:
        if(i==1):
            c+=1
    
    if(c == 9):
        print("\n--- The match is draw ---\n")
        return True
    else:
        return False

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    turn = 1 # 1 for X and 0 for 0
    
    print ("\n---------- Welcome to Tic-Tac-Toe ----------\n")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print ("X's Chance")
            value = int(input ("Please enter a value-> "))
            if(xState[value] == 1 or zState[value] == 1):
                print("--Repeat--\n")
                continue
            xState[value] = 1
            print()
        else:
            print ("O's Chance")
            value = int(input ("Please enter a value-> "))
            if(xState[value] == 1 or zState[value] == 1):
                print("--Repeat--\n")
                continue
            zState[value] = 1
            print()
        
        k = checkWin(xState,zState)
        f = drawState(xState, zState)
        if k != -1 or f == True:
            break
        
        turn = 1 - (turn)
    
print("\n--- Thank You for playing this game ---\n")