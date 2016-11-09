def load(fileName):
    print "Loading " + fileName
    with open(fileName, "r") as inputFile:
        inputString = inputFile.read().replace('\n', '')
    choices = ""
    for character in inputString:
        if not character in choices:
            choices += character

    return inputString, choices