# EarthWatch Correction Code
# 2016 Kyle Choi

import csv

file_open = input("Please the filename of the document to be read by the program (e.g. magpie.csv)")

data = open(file_open)
data = csv.reader(data)
data = list(data)

count = 0
names = []

for i in data:
    if count == 0:
        count += 1
        headers = i
    else:
        names.append(i[2])
        #print(i[2])

def modify(words):


"""
ideas - auto capitalise, correct names
"""
b = " "
for c in names:
    print(c)
    a=c.split(" ")
    print(len(a))
    if len(a) == 3 or 4:# duplicate name error checking
        print("possible name error")
        if a[0] in a[1:]:
            name_inp = input("A first name is repeated in: '"+b.join(a)+"' Would you like to remove the duplicate? (y/n)")
            if name_inp == "y":
                print(len(a[0]))
                name_conf = input("the new name is '"+c[(len(a[0])+1):]+"' is this correct?")
                if name_conf == "y":
                    print(c[(len(a[0])+1):])
                else:
                    name_change = input("Please enter the name manually")
                    print(name_change)
        elif a[-1] in a [:-2]:
            name_inp = input("A last name is repeated in: '"+b.join(a)+"' Would you like to remove the duplicate?")
            if name_inp == "y":
                print(len(a[-1]))
                name_conf = input("the new name is '" + c[:(len(a[-1])-1)] + "' is this correct?")
    elif len(a) >= 5:
        name_inp = input("It seems '"+c+"' is an unusually large string, would you like to modify it?")
        if name_inp == "y":
            print("friendzoned again")
    else:
        print("Pass")

#print(headers)
