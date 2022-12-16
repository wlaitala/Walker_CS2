'''
author: Walker Laitala
Created: 11/28/2022
Updated: 12/10/2022

Description: Battleship on a budget
Bugs: Sometimes there will be only three ships, presumably because the randints are assigning two ships to the same space
      Needs documentation
'''

def main():
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
    import random
    showboard = [["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"]]                                 #defines the board that is shown to the user ^^^^

    databoard = [["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"]]                                 #defines the board where the data (ships and guesses) are held^^^^

    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"       #Pretty sure you can just do random.randint here
    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"
    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"
    databoard[random.randint(0,5) - 1][random.randint(0,5) - 1] = "🚢"

    counter = 10
    wincounter = 4

    print("Here is what your board looks like: ")

    for row in range(0,5):
        col = 0
        for col in range(0,5):
            print(databoard[row][col], end = " ")   #CHANGE TO SHOWBOARD FOR FINAL SUBMISSION
        print(" ")

    turns(showboard, databoard, counter, wincounter)  #, ship1, ship2, ship3, ship4

def turns(showboard, databoard, counter, wincounter):    #, ship1, ship2, ship3, ship4
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
    def correct(showboard):                                         #function to verify if input is valid
        coordinates = input("What space would you like to guess? (row, column)")     #string, "2,2", where the user wants to put their guy
        if len(coordinates) != 3:                               #if it has more than 3 characters, it is invalid
            print("invalid input, try again")
            correct(showboard)
        elif " " in coordinates:
            print("invalid input, try again")
            correct(showboard)
        elif coordinates[1] != ",":                             #If the second character is not a , it is invalid
            print("invalid input, try again")
            correct(showboard)
        elif int(coordinates[0]) - 1 not in range(0,5):         #if the first character is not 0 1 or 2 then invalid
            print("invalid input, try again")
            correct(showboard)
        elif int(coordinates[2]) - 1 not in range(0,5):         #if the second character is not 0 1 or 2 then it is invalid
            print("invalid input, try again")
            correct(showboard)
        row_coord = int(coordinates.split(",")[0]) - 1          #row_coord = integer, 2, is the first number the user inputs
        col_coord = int(coordinates.split(",")[1]) - 1          #col_coord = integer, 3, is the second number the user inputs
        if showboard[row_coord][col_coord] != "-":              #if the space is open the it will put a character there
            print("this spot has been taken, try again")
            correct(showboard)
        return(coordinates)
    coordinates = correct(showboard)

    row_coord = int(coordinates.split(",")[0]) - 1
    col_coord = int(coordinates.split(",")[1]) - 1

    if databoard[row_coord][col_coord] == "🚢":
        print("here is your board:")
        showboard[int(row_coord)][int(col_coord)] = "🚢"
        for row in range(0,5):
            col = 0
            for col in range(0,5):
                print(showboard[row][col], end = " ")
            print(" ")
        counter = counter - 1
        print("hit!\nyou have " + str(counter) + " moves left")
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Explosion_sound.wav', winsound.SND_FILENAME)
        wincounter -= 1
        print("there are " + str(wincounter) + " ships remaining")
        if wincounter == 0:
            print("You win!")
            exit()
        elif counter == 0:
            print("You Lose")
            exit()
        else:
            turns(showboard,databoard, counter, wincounter)
    else:
        print("here is your board:")
        showboard[int(row_coord)][int(col_coord)] = "🌊"
        for row in range(0,5):
            col = 0
            for col in range(0,5):
                print(showboard[row][col], end = " ")
            print(" ")
        counter = counter - 1
        print("miss!\nyou have " + str(counter) + " moves left")
        winsound.PlaySound(r'C:\Users\wlaitala25\Documents\GitHub\Battleship\Splash_sound.wav', winsound.SND_FILENAME)
        print("there are " + str(wincounter) + " ships remaining")
        if counter == 0:
            print("You Lose")
            exit()
        else:
            turns(showboard,databoard, counter, wincounter)




'''
    if (row_coord + "," + col_coord) == ship1 or ship2 or ship3 or ship4:
        print("hit! \nhere is your board:")
        showboard[int(row_coord)][int(col_coord)] = "X"
        for row in range(0,5):
            col = 0
            for col in range(0,5):
                print(showboard[row][col], end = " ")
            print(" ")
        counter = counter - 1
        print("you have " + str(counter) + " moves left")
        wincounter -= 1
    elif board
'''



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

#PLayer 1 chooses their ship locations
#Player 2 chooses their ship locations





main()