'''
author: Walker Laitala
Created: 2/15/2023
Updated: 2/15/2023

Description: Gathers the frequency of words in a file
Bugs: Fix parsing error - clean data in both files
'''
import csv
import matplotlib.pyplot as plt 
import pandas as pd

def main():
    run()
def run():
    import csv
    import matplotlib.pyplot as plt 
    import pandas as pd
    filename = input("ShrewText.txt = Taming of the Shrew\nOthello.txt = Othello\nWhat file would you like to run?")
    if filename == "ShrewText.txt":
        playname = "Taming of the Shrew"
    elif filename == "Othello.txt":
        playname = "Othello"
    else:
        print("That is not a valid file name, try again\n")
        run()
    with open("shakespearefreq.csv", 'w') as title:
        title.write("Word, Frequency\n")
    file = open(filename)            #print(f.read())
    d = dict()
    for line in file:
        strings = line.split(" ")
        for word in strings:
            d[word] = d.get(word,0) + 1
    for key in d:
        if d[key] > 20 and len(key) > 4 and ord(key[1]) + 32 != ord(str(key[1]).lower()):
                    #print(str(key).replace('\n', ' '), d[key])

                    with open('shakespearefreq.csv', 'a') as csvfile:
                        csvfile.write(str(key).replace('\n', '') + ", " + str(d[key]) + "\n")

    toread =  pd.read_csv('shakespearefreq.csv')
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    word = toread["Word"]   
    freq = toread[" Frequency"]       
    plt.pie(freq, labels=word, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Frequency of Words in Shakepeare's " + "'" + playname + "'")
    plt.show()

main()
'''

a = dict(sorted(a.items(), key=lamba x:x[1]))

______Algorithm_____

sorted(d.items(), key = lambda x:x[1])
csvfile.write(str(sorted(d.items(), key = lambda x:x[1])).replace('\n', ''))
csvfile.write(str(key).replace('\n', '') + ", " + str(d[key]) + "\n")

Import file
create dictionary for frequency
    Exclude names/speech intro
print top 10 most common words

'''