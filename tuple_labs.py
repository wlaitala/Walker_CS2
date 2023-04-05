'''
tuple labs
NEED to figure out how to write to tuplelist
'''
import urllib.request

#with open("tuple_labs_emaildata.txt", "r") as file:

url = "http://www.py4inf.com/code/mbox-short.txt"

file = str((urllib.request.urlopen(url)).read())
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
#print(d)


with open("tuplelist.txt", 'w') as title: 
        title.write("Count, Email\n")
'''for key in d:                                                                                                                            
    with open('tuplelist.txt', 'a') as tuplelist:                          
        tuplelist.write(str(key) + ", " + str(d[key]) + "\n")'''