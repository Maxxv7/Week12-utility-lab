# Maxim Alvarado
# CSCI 102 - Section E
# Week 12 - Part A

#Function 1:
def PrintOutput(word):
    print("OUTPUT", word)

#Function 2:
def LoadFile(textfile):
    with open(textfile, "r") as text:
        lines = text.read()
        lines = lines.split("\n")
        PrintOutput(lines)

#Function 3:
def UpdateString(string1, string2, index):
    letterlist = []
    for i in string1:
        letterlist.append(i)
    letterlist[index] = string2
    print("OUTPUT", end=" ")
    for x in letterlist:
        print(x, end= "")
    print()
