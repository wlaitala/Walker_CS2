'''
author: Walker Laitala
Created: 11/28/2022
Updated: 12/26/2022

Description: Battleship on a budget
Bugs: Sometimes there will be only three ships, presumably because the randints are assigning two ships to the same space
      Maybe let the users pick their spots in 2 player game?
      Needs mad documentation
'''

def main():
    '''
    Arguments:
        answer: how many players the user would like to play with
    Takes:
        nothing
    Returns:
        nothing, just sends to next function based on user response
    Description:
        Determines whether the user wants to play with one player or two players
    '''
    answer = input("would you like to play with one or two players?")
    if "1" in answer or "one" in answer:
        oneplayer()
    elif "2" in answer or "two" in answer: 
        twoplayer()
    else:
        print("Invalid input - please include the number 1 or 2 in your response")

def oneplayer():
    '''
    Arguments:
        databoard: The board where the data is placed and help
        showboard: The board that is shown to the user
    Takes:
        Nothing
    Returns:
        5x5 board to send to the next function
    Description: 
        Creates the 5x5 board, places 4 dots randomly throughout
    '''
    import random                                               #For the randomization of coordinates
    showboard = [["-","-","-","-","-"],
                 ["-","-","-","-","-"],
                 ["-","-","-","-","-"],
                 ["-","-","-","-","-"],
                 ["-","-","-","-","-"]]                         #defines the board that is shown to the user ^^^^

    databoard = [["-","-","-","-","-"],
                 ["-","-","-","-","-"],
                 ["-","-","-","-","-"],
                 ["-","-","-","-","-"],
                 ["-","-","-","-","-"]]                         #defines the board where the data (ships and guesses) are held^^^^

    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships

    counter = 10                                                #Int, 9, counter for how many turns the user has remaining          #LET USER CHOODE HOW MANY
    wincounter = 4                                              #Int, 3, counter for how many ships are remaining

    print("Here is what your board looks like: ")               #Showing the user the empty board

    printboard(showboard)                                       #Send to print board function

    turns(showboard, databoard, counter, wincounter)            #Must import both boards and both counters

def turns(showboard, databoard, counter, wincounter):           #Function for when the user actually makes their move
    '''
    Arguments:
        row_coord: row coordinates of the user's guess
        col_coord: column coordinates of the user's guess
        databoard: The board that stors where the ships are
        showboard: The board that is shown to the user and stores their hits and misses
        row: placeholder for "for" loop
        col: placeholder for "for" loop
        counter: counter for the amounf of turns the user has remaining
        wincounter: counter for how many more ships the user needs to hit to win
    Takes:
        databoard and showboard from main, also takes counter and wincounter from main
    Returns:
        "hit" or "miss" depending on whether they hit or miss
        "here is your board:"
        prints showboard as it is after the user's guesses
        tells user how many guesses they have remaining
        tells user how many ships are remaining
        If the user has won or lost, tells the user if they have won or lost
    Description:
        Function where the user interacts and takes their turns
    '''
    import winsound
    while True:                                                 #function to verify if input is valid
        coordinates = input("What space would you like to guess? (row, column; ex. 5,1)")     #string, "2,2", where the user wants to put their guy
        if len(coordinates) != 3:                               #if it has more than 3 characters, it is invalid
            print("invalid input, try again")
            continue                                            #Will restart at the beginning of the loop at each continue
        elif " " in coordinates:                                #If there is a space in the input
            print("invalid input, try again")
            continue
        elif coordinates[1] != ",":                             #If the second character is not a , it is invalid
            print("invalid input, try again")
            continue
        elif int(coordinates[0]) - 1 not in range(0,5):         #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            continue
        elif int(coordinates[2]) - 1 not in range(0,5):         #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            continue
        row_coord = int(coordinates.split(",")[0]) - 1          #row_coord = integer, 2, is the first number the user inputs
        col_coord = int(coordinates.split(",")[1]) - 1          #col_coord = integer, 3, is the second number the user inputs
        if showboard[row_coord][col_coord] != "-":              #if the space is open the it will put a character there
            print("this spot has been taken, try again")
            continue
        break                                                   #end the loop, meaning nothing is wrong and this is a valid input

    row_coord = int(coordinates.split(",")[0]) - 1              #convert user's input into coordinates
    col_coord = int(coordinates.split(",")[1]) - 1              #convert user's input into coordinates

    if databoard[row_coord][col_coord] == "🚢":                 #If the sapce that they guessed contains a ship (meaning it is a hit)
        print("here is your board:")
        showboard[int(row_coord)][int(col_coord)] = "🚢"        #Show them the board
        printboard(showboard)                                   #Send to print board function
        counter = counter - 1                                   #Number of turns remaining goes down by 1
        print("hit!\nyou have " + str(counter) + " moves left") #Tells user that their guess was a hit and how many turn they have left
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Explosion_sound.wav', winsound.SND_FILENAME)       #Playing "BOOM" Sound
        wincounter -= 1                                         #wincounter goes down by one because there is one fewer ship remaining
        print("there are " + str(wincounter) + " ships remaining")     #Tells user how many ships are remaining
        if wincounter == 0:                                     #If there are no ships remaining
            print("You win!")                                   #Tell them they've won
            exit()                                              #Stop ther program
        elif counter == 0:                                      #If they have run out of turns and haven't won yet
            print("You Lose\nhere is where your ships were:")   #Tell them that they have lost
            printboard(databoard)                               #Send to print board function
            exit()                                              #Stop the program
        else:                                                   #If they still have any moves remaining AND there are still ships left (neither win nor loss)
            turns(showboard,databoard, counter, wincounter)     #Run it back
    else:                                                       #If the space of their guess is not a ship (meaning they have missed)
        print("here is your board:") 
        showboard[int(row_coord)][int(col_coord)] = "🌊"        #Replace their guess with a water emoji to signify that they missed on that spot
        printboard(showboard)                                   #Send to print board function
        counter = counter - 1                                   #counter goes down by 1 because they have one fewer turn left
        print("miss!\nyou have " + str(counter) + " moves left")#Tell them that they have missed and how many moves they have left
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Splash_sound.wav', winsound.SND_FILENAME)  #Play the "SPLASH" sound effect
        print("there are " + str(wincounter) + " ships remaining")  #Tell them how many ships there are remaining
        if counter == 0:                                        #If counter is 0 (meaning they have run out of turns)
            print("You Lose\nhere is where your ships were:")   #They have lost
            printboard(databoard)                               #Send to print board function
            exit()                                              #Stop the program
        else:                                                   #Otherwise
            turns(showboard,databoard, counter, wincounter)     #Run it back

def twoplayer():
    '''
    Arguments:
        showboard1: The board that holds user 1's guesses and is shown to them
        databoard1: The board that holds user 1's ship locations
        showboard2: The board that holds user 2's guesses and is shown to them
        databoard2: The board that holds user 2's ship locations
        wincounter1: A counter that tells user1 know how many ships are left. Also is used to determine if there is a winner/who it is
        wincoutner2: A counter that tells user2 know how many ships are left. Also is used to determine if there is a winner/who it is
    Takes:
        Nothing
    Returns:
        All the above arguments, creates/determines them and then sends to next function
    Description:
        A function that creates all of the above variables and sends them to the turns2 function
    '''
    import random
    showboard1 = [["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"]]                         #defines the board that is shown to  user1  ^^^^

    databoard1 = [["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"]]                         #defines the board that holds the data for user1 ^^^^
                    
    showboard2 = [["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"]]                         #defines the board that is shown to the user2 ^^^^
                
    databoard2 = [["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"],
                  ["-","-","-","-","-"]]                         #defines the board that holds the data for user2 ^^^^
    
    wincounter1 = 4
    wincounter2 = 4

    databoard1[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard1[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard1[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard1[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships

    databoard2[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard2[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard2[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships
    databoard2[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Setting the coordinates of the ships

    turns2(databoard1, databoard2, showboard1, showboard2, wincounter1, wincounter2)

def turns2(databoard1, databoard2, showboard1, showboard2, wincounter1, wincounter2):
    '''
    Arguments:
        showboard1: The board that holds user 1's guesses and is shown to them
        databoard1: The board that holds user 1's ship locations
        showboard2: The board that holds user 2's guesses and is shown to them
        databoard2: The board that holds user 2's ship locations
        wincounter1: A counter that tells user1 know how many ships are left. Also is used to determine if there is a winner/who it is
        wincoutner2: A counter that tells user2 know how many ships are left. Also is used to determine if there is a winner/who it is
    Takes:
        All the above variables that were created in the previous function
    Returns:
        Nothing, but ends the program when someone wins. This function will run until someone wins
    Description:
        Function where all of the user interaction stuff takes place. All of the guessing and win determination is in this function. 
    '''
    import winsound

    print("PLAYER 1'S TURN")

    print("Here is what your guessboard looks like: ")          #Showing the user the empty board

    printboard(showboard1)                                      #Send to print board function

    while True:                                                 #function to verify if input is valid
        coordinates = input("What space would you like to guess? (row, column; ex. (5,1)")     #string, "2,2", where the user wants to put their guy
        if len(coordinates) != 3:                               #if it has more than 3 characters, it is invalid
            print("invalid input, try again")
            continue                                            #Will restart at the beginning of the loop at each continue
        elif " " in coordinates:                                #If there is a space in the input
            print("invalid input, try again")
            continue
        elif coordinates[1] != ",":                             #If the second character is not a , it is invalid
            print("invalid input, try again")
            continue
        elif int(coordinates[0]) - 1 not in range(0,5):         #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            continue
        elif int(coordinates[2]) - 1 not in range(0,5):         #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            continue
        row_coord = int(coordinates.split(",")[0]) - 1          #row_coord = integer, 2, is the first number the user inputs
        col_coord = int(coordinates.split(",")[1]) - 1          #col_coord = integer, 3, is the second number the user inputs
        if showboard1[row_coord][col_coord] != "-":              #if the space is open the it will put a character there
            print("this spot has been taken, try again")
            continue
        break                                                   #end the loop, meaning nothing is wrong and this is a valid input

    row_coord = int(coordinates.split(",")[0]) - 1              #convert user's input into coordinates
    col_coord = int(coordinates.split(",")[1]) - 1              #convert user's input into coordinates

    if databoard2[row_coord][col_coord] == "🚢":                #If the sapce that they guessed contains a ship (meaning it is a hit)
        print("here is your guessboard:")
        showboard1[int(row_coord)][int(col_coord)] = "🚢"       #Show them the board
        printboard(showboard1)                                  #Send to print board function
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Explosion_sound.wav', winsound.SND_FILENAME)       #Playing "BOOM" Sound
        wincounter1 -= 1                                         #wincounter goes down by one because there is one fewer ship remaining
        if wincounter1 == 0:                                     #If there are no ships remaining
            print("You win!")                                   #Tell them they've won
            exit()                                              #Stop ther program
    else:
        print("miss!")
        showboard1[int(row_coord)][int(col_coord)] = "🌊"        #Replace their guess with a water emoji to signify that they missed on that spot
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Splash_sound.wav', winsound.SND_FILENAME)  #Play the "SPLASH" sound effect
    
    print("here is your updated board: ")
    printboard(showboard1)                                       #Send to print board function
    print("there are " + str(wincounter1) + " ships remaining\n")  #Tell them how many ships there are remaining

    print("PLAYER 2'S TURN")

    print("Here is what your guessboard looks like: ")          #Showing the user the empty board

    printboard(showboard2)                                       #Send to print board function

    while True:                                                 #function to verify if input is valid
        coordinates = input("What space would you like to guess? (row, column; ex. (5,1)")     #string, "2,2", where the user wants to put their guy
        if len(coordinates) != 3:                               #if it has more than 3 characters, it is invalid
            print("invalid input, try again")
            continue                                            #Will restart at the beginning of the loop at each continue
        elif " " in coordinates:                                #If there is a space in the input
            print("invalid input, try again")
            continue
        elif coordinates[1] != ",":                             #If the second character is not a , it is invalid
            print("invalid input, try again")
            continue
        elif int(coordinates[0]) - 1 not in range(0,5):         #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            continue
        elif int(coordinates[2]) - 1 not in range(0,5):         #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            continue
        row_coord = int(coordinates.split(",")[0]) - 1          #row_coord = integer, 2, is the first number the user inputs
        col_coord = int(coordinates.split(",")[1]) - 1          #col_coord = integer, 3, is the second number the user inputs
        if showboard2[row_coord][col_coord] != "-":              #if the space is open the it will put a character there
            print("this spot has been taken, try again")
            continue
        break                                                   #end the loop, meaning nothing is wrong and this is a valid input

    row_coord = int(coordinates.split(",")[0]) - 1              #convert user's input into coordinates
    col_coord = int(coordinates.split(",")[1]) - 1              #convert user's input into coordinates

    if databoard1[row_coord][col_coord] == "🚢":               #If the sapce that they guessed contains a ship (meaning it is a hit)
        print("here is your guessboard:")
        showboard2[int(row_coord)][int(col_coord)] = "🚢"      #Show them the board
        printboard(showboard2)                                  #Send to print board function
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Explosion_sound.wav', winsound.SND_FILENAME)       #Playing "BOOM" Sound
        wincounter2 -= 1                                        #wincounter goes down by one because there is one fewer ship remaining
        if wincounter2 == 0:                                    #If there are no ships remaining
            print("You win!")                                   #Tell them they've won
            exit()                                              #Stop ther program
    else:
        print("miss!")
        showboard2[int(row_coord)][int(col_coord)] = "🌊"       #Replace their guess with a water emoji to signify that they missed on that spot
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Splash_sound.wav', winsound.SND_FILENAME)  #Play the "SPLASH" sound effect
        
    print("here is your updated board: ")
    printboard(showboard2)                                       #Send to print board function
    print("there are " + str(wincounter1) + " ships remaining\n")#Tell them how many ships there are remaining

    turns2(databoard1, databoard2, showboard1, showboard2, wincounter1, wincounter2)

def printboard(board):
    '''
    Simple algorithm to print board
    '''

    for row in range(0,5):                                                      #Test every row,
        col = 0                                                                 #While the column is 0
        for col in range(0,5):                                                  #Test every column
            if col != 4:                                                        #ONLY if it is not the last column
                if board[row][col + 1] == "🌊" or board[row][col + 1] == "🚢": #If the NEXT character in the sequence is an emoji,
                    print(board[row][col], end = ' ')                           #Print one less space after this character
                else:                                                           #If the nect character isn't an emoji,
                    print(board[row][col], end = '  ')                          #Print the regular amount of spaces
            else:                                                               #If it is printing from the very last column, obviously the nect character can't be an emoji
                print(board[row][col], end = '  ')                              #So print the regular amount of spaces
        print(' ')                                                              #print " " for the code to recognize the ending

main()                                                                          #Main baby
    

#________Tentative Algorithm__For Reg____________________

#Main
    #Create 5x5 board
    #Place 4 dots randomly throughout
    #send board to telling the user

#Telling the user
    #Show the user what the board looks like
    #Tell the user how many turns they have left (starting wiht 10)
    #Send to user takes a turn

#User takes a turn
    #Get user coordinates   
    #Determine if coordinates are valid
        #Is a spot on the board
        #Is not taken by a guess already
        #Make this it's own function???
    #Determine if they are a hit/miss
        #if hit, replace with X
            #win counter adds one
            #if win counter == 4, user wins
            #turns remaining goes down by one
            #is turns remaining == 0, user loses
        #if miss, replace with O
            #turns remaining goes down by one
            #is turns remaining == 0, user loses

#__________TENTATIVE FOR TWO PLAYER_______

#Gameplay: 
    #PLayer 1 chooses their ship locations
    #Player 2 chooses their ship locations

    #Player 1 guesses a coordinate on player 2's board
    #They are told if it is a hit or a miss
        #Check for win condition
            #If they have guessed all of the ships
        #They are told all of their info
            #Board, moves left, ships left

    #Player 2 guesses a coordinate on player 2's board
    #They are told if it is a hit or a miss
        #Check for win condition
            #If they have guessed all of the ships
        #They are told all of their info
            #Board, moves left, ships left
    

#Code:

    #Creation():
        #Create boards
            #1databoard, 1showboard, 2databoard, 2showboard
        #Create counters   
            #1wincounter, 2wincounter

        #Tell player 1 to input the coordinates of where they want their 5 ships
        #Set 1databoard with all of their ships
        
        #Tell player 2 to input the coordinates of where they want their 5 ships
        #Set 2databoard with all of their ships

        #Send to next function
    #2pmoves():
        #Show player 1 their 1showboard
        #Ask player 1 for their guess coordinates
        #Verify to check if they are valid
        #See if it is hit or miss and tell them
        #Check if they have won
        #Show them their board
        #Tell them their info
            #turns remaining, ships remaining
        
        #Show player 2 their 2showboard
        #Ask player 2 for their guess coordinates
        #Verify to check if they are valid
        #See if it is hit or miss and tell them
        #Check if they have won
        #Show them their board
        #Tell them their info
            #turns remaining, ships remaining