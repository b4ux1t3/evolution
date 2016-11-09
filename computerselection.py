# This is the genetic algorithm minus all of the extra crap from the testing

import random       
import sentiment-analysis as sa


#TODO This needs to use the sentiment analysis tool to generate a score.
def calcFitness(member):
    fitness = 0
    # Run sentiment analysis here
    fitness = sa.parse(member)
    # Then calculate fitness
    
    # Finally, return fitness
    return fitness

def buildFitnessDictionary(population):
    fitdict = {}
    for member in population:
        fitdict[member] = calcFitness(member)
    return fitdict

def createGenePool(fitnessDictionary):
    total = 0
    highestFitness = 0
    genePool = []

    # First go through and figure out which has the highest fitness
    for member in fitnessDictionary:
            if fitnessDictionary[member] > highestFitness:
                highestFitness = fitnessDictionary[member]

    # Then go through and add each member to the gene pool at a frequency equal to its percentage of the highest fitness score.
    for member in fitnessDictionary:
        counter = 0
        while counter < int(len(range(fitnessDictionary[member])) / float(highestFitness) * 100):
            genePool.append(member)
            counter += 1
    return genePool

def mutate(offspring):
    global choices, mutationRate
    index = 0
    for gene in offspring:
        if random.randrange(1, 1000) < mutationRate:
            offspring = offspring[:index] + random.choice(choices) + offspring[index + 1:]
            index += 1   
    return offspring

def breed(genePool):
    
    mother = random.choice(genePool)
    father = random.choice(genePool)

    while mother == father:
        father = random.choice(genePool)

    # Midpoint is middle of mother +/- a random number 
    #midpoint = random.randrange((len(mother) / 2) - (len(mother) / 4), (len(mother) / 2) + (len(mother) / 4))
    # That was a bad idea for this particular problem. Keep it just in case

    # Now midpoint is just anywhere from index 1 to -2
    # That means there will always be at least one character at the beginning or end from eachg parent
    # TODO: Make it take rabndom chunks from the string each iteration
    midpoint = random.randrange(1, len(mother) - 1)
    offspring = mother[:midpoint] + father[midpoint:]
    mutate(offspring)
    return offspring

def breedPopulation(populationSize,  genePool):
    population = []
    for i in range(populationSize):
        population.append(breed(genePool))
    
    return population