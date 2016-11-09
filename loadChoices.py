# Loads a text file full of words into a list so each element is a word

def load(fileName):
    print "Loading " + fileName
    with open(fileName, "r") as inputFile:
        for line in inputFile:
            choices.append(line.strip())

    return choices