# https://github.com/Maxxv7/Week12-utility-lab
# Maxim Alvarado
# CSCI 102 - Section E
# Week 12 - Part B

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

#Function 4:
HCList = ["Hi there", "word word word!", "Word word", "things", "things"] #For testing purposes
def FindWordCount(lizt, stryng):
    wordcount = 0
    newlizt = []
    bestlizt = []
    for x in lizt:
        newlizt.append(x.split(" ")) #separate list into individual words
    for z in newlizt:
        bestlizt = bestlizt + z #Turn list of lists into one list
    for i in bestlizt:
        if i == stryng:
            wordcount += 1 #Adds one to word count if the word is in the list
    PrintOutput(wordcount)
    
#Function 5:
def ScoreFinder(list1, list2, string):
    playernum = -1
    for i in range(0, len(list1)):
        if list1[i].lower() == string.lower():
            playernum = i
    if playernum > -1:
        print("OUTPUT", list1[playernum], "got a score of", list2[playernum])
    elif playernum == -1:
        PrintOutput("player not found")

#Function 6:
def Union(list1, list2):
    for i in list1:
        for x in list2:
            if x == i:
                list2.remove(x)
    onion = list1 + list2
    return onion
    
#Function 7:
def Intersection(list1, list2):
    intersection = []
    for i in list1:
        for x in list2:
            if x == i:
                intersection.append(x)
    return intersection

#Function 8:
def NotIn(list1, list2):
    newlist = []
    for z in list1:
        newlist.append(z)
    for i in list1:
        for x in list2:
            if x == i:
                newlist.remove(i)
    return newlist














