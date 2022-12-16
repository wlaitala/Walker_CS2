'''
author: Walker Laitala
Created: 11/15/2022
Updated: 12/10/2022

Description: Tic Tac Toe!
Bugs: None Known
'''

def main():
    '''
    Arguments:
        board: list, is the board
    Takes: 
        Input from users, is a coordinate of two numbers between 1 and 3 seperated by a comma
    Returns:   
        Nothing, sends to next function
    Description: test
        Prints the board, sends to next function. Is the main
    '''
    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]                                 #This is the board^^

    moves(board)                                            #run the moves function

def moves(board):                                           #defines the moves function
    
    def xcorrect():                                         #function to verify if input is valid
        x_input = input("Player X input(row,column): ")     #string, "2,2", where the user wants to put their guy
        if len(x_input) != 3:                               #if it has more than 3 characters, it is invalid
            print("invalid input, try again")
            xcorrect()
        elif " " in x_input:                                #If there is a " ", invalid
            print("invalid input, try again")
            xcorrect()
        elif x_input[1] != ",":                             #If the second character is not a , it is invalid
            print("invalid input, try again")
            xcorrect()
        elif int(x_input[0]) - 1 not in range(0,3):         #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            xcorrect()
        elif int(x_input[2]) - 1 not in range(0,3):         #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            xcorrect()
        rowinput = int(x_input.split(',')[0]) - 1           #rowinput = integer, 2, is the first number the user inputs
        colinput = int(x_input.split(',')[1]) - 1           #colinput = integer, 3, is the second number the user inputs
        if board[rowinput][colinput] != "-":                #if the space is open the it will put a character there
            print("this spot has been taken, try again")
            xcorrect()
        return(x_input)
    xreturn = xcorrect()                                    #run the function
    
    board[int(xreturn.split(",")[0]) - 1][int(xreturn.split(",")[1]) - 1] = "X"
    for row in range(3):                                    #a for loop to print the board that goes through every space in the board and prints it
        col = 0                                             #set col as 0 as a baseline
        for col in range(3):                                #nested for loop to handle the column
            print(board[row][col], end = " ")               #actually printing the board
        print(' ')                                          #print a " " after eacher character to make it look pretty

    iswin = win(board)                                      #iswin is equal to return of win function
    if iswin != False:                                      #if the win function does not return false (meaning someone has won)...
        print(iswin + " wins!")                             #print the return of win function and "wins!"
        exit()                                              #stop running

    if "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:          #If '-' isn't in the board anywhere, it must be a tie
        print("it's a tie!")                                #so say it's a tie
        exit()                                              #exit program

    def ocorrect():                                         #function to verify if input is valid
        o_input = input("Player O input(row,column): ")     #string, "2,2", where the user wants to put their guy
        if len(o_input) != 3:                               #if it has more than 3 characters, it is invalid
            print("invalid input, try again")
            ocorrect()
        elif o_input[1] != ",":                             #If the second character is not a , it is invalid
            print("invalid input, try again")
            ocorrect()
        elif int(o_input[0]) - 1 not in range(0,3):         #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            ocorrect()
        elif int(o_input[2]) - 1 not in range(0,3):         #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            ocorrect()
        rowinput = int(o_input.split(',')[0]) - 1           #rowinput = integer, 2, is the first number the user inputs
        colinput = int(o_input.split(',')[1]) - 1           #colinput = integer, 3, is the second number the user inputs
        if board[rowinput][colinput] != "-":                #if the space is open the it will put a character there
            print("invalid input, try again")
            ocorrect()
        return(o_input)                                     #return the coordinated because they are good to go
        
    oreturn = ocorrect()                                    #run the function
    
    board[int(oreturn.split(",")[0]) - 1][int(oreturn.split(",")[1]) - 1] = "O"         #set the coordinates to be their character

    for row in range(3):                                    #a for loop to print the board that goes through every space in the board and prints it
        col = 0                                             #set col as 0 as a baseline
        for col in range(3):                                #nested for loop to handle the column
            print(board[row][col], end = " ")               #actually printing the board
        print(' ')                                          #print a " " after eacher character to make it look pretty

    iswin = win(board)                                      #iswin is equal to return of win function
    if iswin != False:                                      #if the win function does not return false (meaning someone has won)...
        print(iswin + " wins!")                             #print the return of win function and "wins!"
        exit()                                              #stop running

    moves(board)                                            #run the function
def win(board):                                             #define win function
    '''
    Arguments:
        i: Just a temporary varibale to iterate through range(3), 2
        board: The board as it is when imported into function, list
    Takes:
        the board variable from moves function
    Returns:
        Returns the string "X" or "O" (if it has determined someone has won), or False (if no one has won)
    Description:
        A funtion to determine whether or not someone has won or not, and if someone has won then determine who has won
    '''
    for i in range(3):                                              #for 0, 1, and 2
        if board[i][0] == board[i][1] == board[i][2] != "-":        #if the entire row equals eachother and doesn't equal "-", then that means someone won
            return(board[i][0])                                     #any of those spaces contaitn the character of the winning team
        elif board[0][i] == board[1][i] == board [2][i] != "-":     #if the entire column equals eachother and doesn't equal "-", then that means someone won
            return(board[0][i])                                     #any of those spaces contaitn the character of the winning team
    if board[0][0] == board[1][1] == board[2][2] != "-":            #if the diagonal is all the same then someone won
        return(board[0][0])                                         #any of those spaces contaitn the character of the winning team
    if board[0][2] == board [1][1] == board[2][0] != "-":           #if the diagonal is all the same then someone won
        return(board[0][0])                                         #any of those spaces contaitn the character of the winning team
    return(False)
main()