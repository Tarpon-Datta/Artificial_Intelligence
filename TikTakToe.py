def gameboard(Max, Min):
    zero = 'X' if Max[0] else ('O' if Min[0] else 0)
    one = 'X' if Max[1] else ('O' if Min[1] else 1)
    two = 'X' if Max[2] else ('O' if Min[2] else 2)
    three = 'X' if Max[3] else ('O' if Min[3] else 3)
    four = 'X' if Max[4] else ('O' if Min[4] else 4)
    five = 'X' if Max[5] else ('O' if Min[5] else 5)
    six = 'X' if Max[6] else ('O' if Min[6] else 6)
    seven = 'X' if Max[7] else ('O' if Min[7] else 7)
    eight = 'X' if Max[8] else ('O' if Min[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 
    
def sum(a, b, c ):
    return a+b+c

def checkWin(Max, Min):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
            [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(Max[win[0]], Max[win[1]], Max[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(Min[win[0]], Min[win[1]], Min[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    Max = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Min = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1                          # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        gameboard(Max, Min)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            Max[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            Min[value] = 1
        cwin = checkWin(Max, Min)
        if(cwin != -1):
            print("Match over")
            break
        turn = 1 - turn