'''
tuple labs
'''
import urllib.request

#with open("tuple_labs_emaildata.txt", "r") as file:

url = "http://www.py4inf.com/code/mbox-short.txt"

file = str((urllib.request.urlopen(url)).read())

def main():
    print("SELECT PROGRAM")
    answer = input("what program would you like to run?\nfrequency - count # emails from each sender\ntime - # emails each time of day\nletters - frequency of letters\n")

    if answer == "frequency":
        frequency()
    elif answer == "time":
        time()
    elif answer == "letters":
        letters()
    else:
        main()
def frequency():
    d = dict()
    lines = file.split("\n")
    for i in lines:
        words = str(lines).split(" ")
        for number in range(0,len(words)):
            if "From" in words[number]:
                address = words[number + 1].strip("\\nSubject:")
                if address not in d:
                    d[address] = 1
                else:
                    d[address] = d[address] + 1
    inv_map = {}
    for k, v in d.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    pairs = (sorted(inv_map.items(), key=lambda x: x[0]))

    with open("tuplelist.txt", 'w') as title: 
            title.write("Count, Email\n")
    for number in range(0,len(pairs)):
        with open('tuplelist.txt', 'a') as tuplelist:                     
            tuplelist.write(str(pairs[number]).strip("(").strip(")").replace("[", '').strip("]") + "\n")

    #REGULAR PRINT W/O SORTING VVV
    '''with open("tuplelist.txt", 'w') as title: 
            title.write("Count, Email\n")
    for key in d:                                                                                                     
        with open('tuplelist.txt', 'a') as tuplelist:                     
            tuplelist.write(str(d[key]) + ", " + str(key) + "\n")'''

def time():
    d = dict()
    lines = file.split("\n")
    for i in lines:
        words = str(lines).split(" ")
        for number in range(0,len(words)):
            if "wed" in words[number].lower() or "thu" in words[number].lower() or "fri" in words[number].lower() or "sat" in words[number].lower():
                time = words[number + 4]
                time = time[0:2]
                if time[0] == "0" or time[0] == "1" or time[0] == "2":
                    if time not in d:
                        d[time] = 1
                    else:
                        d[time] = d[time] + 1

    pairs = (sorted(d.items(), key=lambda x: x[0]))

    with open("tuplelist.txt", 'w') as title: 
            title.write("Time, Freq\n")
    for number in range(0,len(pairs)):
        with open('tuplelist.txt', 'a') as tuplelist:                     
            tuplelist.write(str(pairs[number]).strip("(").strip(")") + "\n")
    
def letters():
    '''
    get file
    dictionary
    sort
    '''
    d = dict()
    
    for number in range(0,len(file)):
        key = file[number].lower()
        if (ord(key) <= 122 and ord(key) >= 97):
            if key not in d:
                d[key] = 1
            else:
                d[key] = d[key] + 1

    pairs = (sorted(d.items(), key=lambda x: x[0]))

    with open("tuplelist.txt", 'w') as title: 
            title.write("Letter, Freq\n")
    for number in range(0,len(pairs)):
        with open('tuplelist.txt', 'a') as tuplelist:                     
            tuplelist.write(str(pairs[number]).strip("(").strip(")") + "\n")
    

main()