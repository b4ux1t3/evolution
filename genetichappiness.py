# This program will generate tweets (140 characters or less) that, 
# and then run a sentiment analysis on teh generate tweets, and 
# then select for happier tweets. IN the end, the happiest tweet after
# a given period of time will be tweeted.

import computerselection as darwin
from loadChoices import load
from sys import argv
choices = []

#TODO: Change this so it no longer assumes a string
# Takes in a population size and a file name, and returns a population to breed
def initPopulation(populationSize):
    global choices

    choices = load(argv[1])

    population = []
    for i in range(populationSize):
        population.append("")
        for j in range(len(goal)):
            population[i] += random.choice(choices)
    return population 

