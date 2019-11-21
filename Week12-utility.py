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
        return lines
