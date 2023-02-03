'''
author: Walker Laitala
Created: 1/14/2023
Updated: 1/31/2023

Description: Interface where the users take their turns and do everything
Bugs: Spacing
'''

def main():
    '''
    
    '''

    board = [["-","-","-","-","-","-","-"],
             ["-","-","-","-","-","-","-"],
             ["-","-","-","-","-","-","-"],
             ["-","-","-","-","-","-","-"],
             ["-","-","-","-","-","-","-"],
             ["-","-","-","-","-","-","-"],
             ["-","-","-","-","-","-","-"]]
    
    turns(board)

def turns(board):
    '''
    Arguments:
        Board: The board where all the moves are stored and presented

    Takes:
        Nothing
    Returns:
        board to next function
    Description:
        Players take their turns until someone wins. Win condition is from a seperate function
    '''

    while True:
        answer = input("Player 1, where would you like to move?")
        if len(answer) != 3:
            print("invalid input, try again")
            continue
        elif answer[1] != ",":                         #If the second character is not a , it is invalid
            print("invalid input, try again")
            continue
        elif int(answer[0]) - 1 not in range(0,5):     #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            continue
        elif int(answer[2]) - 1 not in range(0,7):     #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            continue
        break

    row_coord = int(answer.split(",")[0]) - 1          #row_coord = integer, 2, is the first number the user inputs
    col_coord = int(answer.split(",")[1]) - 1          #col_coord = integer, 3, is the second number the user inputs

    board[row_coord][col_coord] = "🔴"

    for row in range(0,5):
        col = 0
        for col in range(0,7):
            if col != 6:
                if board[row][col + 1] == "🔴" or board[row][col + 1] == "🟡":
                    print(board[row][col], end = ' ')
                else:
                    print(board[row][col], end = '  ')
            else:
                print(board[row][col], end = '  ')
        print(' ')

    while True:
        answer = input("Player 2, where would you like to move?")
        if len(answer) != 3:
            print("invalid input, try again")
            continue
        elif answer[1] != ",":                         #If the second character is not a , it is invalid
            print("invalid input, try again")
            continue
        elif int(answer[0]) - 1 not in range(0,5):     #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            continue
        elif int(answer[2]) - 1 not in range(0,7):     #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            continue
        break

    row_coord = int(answer.split(",")[0]) - 1          #row_coord = integer, 2, is the first number the user inputs
    col_coord = int(answer.split(",")[1]) - 1          #col_coord = integer, 3, is the second number the user inputs

    board[row_coord][col_coord] = "🟡"

    for row in range(0,5):
        col = 0
        for col in range(0,7):
            if col != 6:
                if board[row][col + 1] == "🔴" or board[row][col + 1] == "🟡":
                    print(board[row][col], end = ' ')
                else:
                    print(board[row][col], end = '  ')
            else:
                print(board[row][col], end = '  ')
        print(' ')

    turns(board)

main()