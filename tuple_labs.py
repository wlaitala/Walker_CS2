'''
tuple labs
'''
import urllib.request                                                                      #import this for reading file via URL

file = str((urllib.request.urlopen("http://www.py4inf.com/code/mbox-short.txt")).read())   #setting the data as file universally                     
d = dict()                                                                                 #Making d be a dictionary universally

def main():                                                                                #def main
    print("SELECT PROGRAM")                                                                #Just for a little UI action
    answer = input("what program would you like to run?\nfrequency - count # emails from each sender\ntime - # emails each time of day\nletters - frequency of letters\n") #More UI action

    if answer == "frequency":                                                              #Next few lines are just so the user can run whichever function they want
        frequency()                                                                        #  ^
    elif answer == "time":                                                                 #  ^^
        time()                                                                             #  ^^^
    elif answer == "letters":                                                              #  ^^^^
        letters()                                                                          #  ^^^^^
    else:                                                                                  #  ^^^^^^
        main()                                                                             #  ^^^^^^^
def frequency():                                                                           #Function for email frequency
    lines = file.split("\n")                                                               #list, "random line of datasheet", basically just a list of the lines of the program
    words = str(lines).split(" ")                                                          #list, "From", words is a list of all the different words in the datasheet
    for number in range(0,len(words)):                                                     #for loop that iterates through every word in the datasheet
        if "From" in words[number]:                                                        #Basically if "From" = the word that the for loop is on,
            address = words[number + 1].strip("\\nSubject:")                               #Then the next word is an email address, so set address as such (string, "example@gmail.net, email address")
            if address not in d:                                                           #If address is not in the dictionary yet,
                d[address] = 1                                                             #set it as 1 in the dictionary
            else:                                                                          #But if it already exists,
                d[address] = d[address] + 1                                                #Its value in the dictionary is increased by 1
    inv_map = {}                                                                           #Lines 31-33 were foudn online. Their purpose is to invert the dictionary mappings
    for k, v in d.items():                                                                 # ^
        inv_map[v] = inv_map.get(v, []) + [k]                                              # ^^
    pairs = (sorted(inv_map.items(), key=lambda x: x[0]))                                  #list, "example@gmail.com: 3", basically sorts the dictionary using lambda function. ALSO converts dictionary to list

    with open("tuplelist.txt", 'w') as tuplelist:                                          #Open the write file as tuplelist
        tuplelist.write("Count, Email\n")                                                  #write "Count, Email"
        for number in range(0,len(pairs)):                                                 #for loop that iterates through the length of pairs       
            tuplelist.write(str(pairs[number]).strip("(").strip(")").replace("[", '').strip("]") + "\n")    #write each item in pairs

    #REGULAR PRINT W/O SORTING JUST IN CASE VVV
    '''with open("tuplelist.txt", 'w') as title: 
            title.write("Count, Email\n")
    for key in d:                                                                                                     
        with open('tuplelist.txt', 'a') as tuplelist:                     
            tuplelist.write(str(d[key]) + ", " + str(key) + "\n")'''

def time():                                                                                #Function for sorting by time of send
    lines = file.split("\n")                                                               #list, "random line of datasheet", basically just a list of the lines of the program
    words = str(lines).split(" ")                                                          #list, "From", words is a list of all the different words in the datasheet
    for number in range(0,len(words)):                                                     #for loop that iterates through every word in the datasheet
        if "wed" in words[number].lower() or "thu" in words[number].lower() or "fri" in words[number].lower() or "sat" in words[number].lower():    #These are the only days that appear, and they are all written w/ 3 letters
            time = words[number + 4]                                                       #There is a timestamp that appears 4 words after, so that is set as time (string, "06:45:32", a timestamp)
            time = time[0:2]                                                               #Take the first two characters, because these represent the hour
            if time[0] == "0" or time[0] == "1" or time[0] == "2":                         #Only accept if the first digit is 0, 1, or 2 because otherwise that is not a valid time
                if time not in d:                                                          #if time is not already a part of the dictionary,
                    d[time] = 1                                                            #then set its dictionary value as 1
                else:                                                                      #but if it already exists,
                    d[time] = d[time] + 1                                                  #Increase its value by 1

    pairs = (sorted(d.items(), key=lambda x: x[0]))                                        #Sorting the dictionary and converting it to a list

    with open("tuplelist.txt", 'w') as tuplelist:                                          #opening the file as tuplelist
        tuplelist.write("Time, Freq\n")                                                    #Writing to that file                                       #opening the file as tuplelist
        for number in range(0,len(pairs)):                                                 #iterating through every item of pairs (the old dictionary)
            tuplelist.write(str(pairs[number]).strip("(").strip(")") + "\n")               #write every item of pairs to the tuplelist file
    
def letters():                                                                             #function for gathering each letter and its frequency in the datasheet
    for number in range(0,len(file)):                                                      #iterating through the length of file (each individual chaarcter)
        key = file[number].lower()                                                         #string, "f", setting key as each character in the datasheet (and .lowered)
        if (ord(key) <= 122 and ord(key) >= 97):                                           #if key is a letter,
            if key not in d:                                                               #Then all good so continue with normal dictionary mapping. if it is not already in dictionary,
                d[key] = 1                                                                 #then set it as 1 in the dictionary
            else:                                                                          #otherwise,
                d[key] = d[key] + 1                                                        #increase its value by 1

    pairs = (sorted(d.items(), key=lambda x: x[0]))                                        #sorting the dictionary and converting it to a list

    with open("tuplelist.txt", 'w') as tuplelist:                                          #open the file and set it as tuplelist
        tuplelist.write("Letter, Freq\n")                                                  #write that stuff to the file                                        #open the file as tuplelist
        for number in range(0,len(pairs)):                                                 #iterate through length of pairs
            tuplelist.write(str(pairs[number]).strip("(").strip(")") + "\n")               #write each itme of pairs to the file
main()                                                                                     #file