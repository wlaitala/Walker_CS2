'''
author: Walker Laitala
Created: 2/15/2023
Updated: 2/15/2023

Description: Gathers the frequency of words in a file
Bugs: None
'''
import csv
import matplotlib.pyplot as plt 
import pandas as pd

def main():
    '''
    Does not really accomplish anything, just is a main function that runs the next function
    '''
    run()
def run():
    '''
    Takes: Nothing
    Returns: Nothing, but opens a chart
    Arguments: None
    Description: Reads a file and creates a pie chart of its most frequent words
    '''
    import csv                                                  #Importing all the necessary things
    import matplotlib.pyplot as plt                             #Importing all the necessary things
    import pandas as pd                                         #Importing all the necessary things
    filename = input("ShrewText.txt = Taming of the Shrew\nOthello.txt = Othello\nWhat file would you like to run?")    #Allowing the user to choose what file they want to run
    if filename == "ShrewText.txt":                             #if they choose the taming of the shrew,
        playname = "Taming of the Shrew"                        #playname will be Taming of the Shrew (for the title of the graph)
    elif filename == "Othello.txt":                             #if they choose Othello,
        playname = "Othello"                                    #playname will be Taming of the Shrew (for the title of the graph)
    else:
        print("That is not a valid file name, try again\n")     #If they type in something incorrect
        run()                                                   #Retry
    with open("shakespearefreq.csv", 'w') as title:             #Opening a new document to write to
        title.write("Word, Frequency\n")                        #Write "Word, Frequency" to it (so it can be read easier later)
    file = open(filename)            #print(f.read())           #set the file as file variable
    d = dict()                                                  #set d as a dictionary
    for line in file:                                           #For each line in the play
        strings = line.split(" ")                               #Strings = list of each individual word
        for word in strings:                                    #word is each individual word
            d[word] = d.get(word,0) + 1                         #Setting them as frequencies in a dictionary
    for key in d:                                               #for each key in the dictionary
        if d[key] > 20 and len(key) > 4 and ord(key[1]) + 32 != ord(str(key[1]).lower()):      #If there are more than 20 and it is longer than 4 chars
                                                                                               #and the second letter isn't capitalized (to eliminate introductions)
                    with open('shakespearefreq.csv', 'a') as csvfile:                          #set csvfile as the doc we wrote to
                        csvfile.write(str(key).replace('\n', '') + ", " + str(d[key]) + "\n")  #write in all of the keys from the dictionary along with their value
    toread =  pd.read_csv('shakespearefreq.csv')                                               #Use the pandas function to read the temporary write file
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]                           #Setting the colors of the wheel
    word = toread["Word"]                                                                      #The first column
    freq = toread[" Frequency"]                                                                #The second column
    plt.pie(freq, labels=word, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)  #Lots of fancy stuff that I don't entirely understand
    plt.title("Frequency of Words in Shakepeare's " + "'" + playname + "'")                    #The title of the chart
    plt.show()                                                                                 #Show the chart

main()

'''
a = dict(sorted(a.items(), key=lamba x:x[1]))

______Trash Algorithm_____

sorted(d.items(), key = lambda x:x[1])
csvfile.write(str(sorted(d.items(), key = lambda x:x[1])).replace('\n', ''))
csvfile.write(str(key).replace('\n', '') + ", " + str(d[key]) + "\n")

Import file
create dictionary for frequency
    Exclude names/speech intro
print top  most common words
put into chart

'''