import random
from datetime import datetime
import sys
from loadTextFile import load

goal = "to be or not to be that is the question"
choices = "abcdefghijklmnopqrstuvwxyz "
populationSize = 1000
mutationRate = 200

def initPopulation(populationSize):
    global choices, goal
    population = []
    for i in range(populationSize):
        population.append("")
        for j in range(len(goal)):
            population[i] += random.choice(choices)
    return population        

def calcFitness(member):
    global goal
    fitness = 0
    index = 0
    for gene in member:
        if member[index] == goal[index]:
            fitness += 1
        index += 1
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
    for character in offspring:
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
# Returns true if there is a second argument, which can only be a file name.
def checkArgs():
    return len(sys.argv) == 2

def main():
    global goal, choices, populationSize

    if checkArgs():
        goal, choices = load(sys.argv[1])
    
    highestFitness = 0
    population = initPopulation(populationSize)
    generation = 0
    startTime = datetime.now()
    targetFitness = len(goal)
    while highestFitness < targetFitness:

        print "Generation " + str(generation) + "\n"
        genTime = datetime.now()
        fitnessScores = buildFitnessDictionary(population)
        genePool = createGenePool(fitnessScores)
        print "Gene pool built in " + str(datetime.now() - genTime) + "\n"

        # Check the fitnesses of the members of the population
        for member in fitnessScores:
            if fitnessScores[member] > highestFitness:
                highestFitness = fitnessScores[member]
                #print member + "\nFitness: " + str(highestFitness) + "/" + str(targetFitness)

        # Report average fitness
        total = 0.0
        for i in fitnessScores:
            total += fitnessScores[i]
        print "Average fitness score: " + str(total / len(fitnessScores)) + " / " + str(targetFitness) + "\n" + "Max fitness score: " + str(highestFitness) + "\n"

        # Make a new population
        popTime = datetime.now()
        population = breedPopulation(populationSize, genePool)
        print "New population bred in " + str(datetime.now() - popTime) + "\n"
        print "Time elapsed: " + str(datetime.now() - startTime) + "\n" + "-" * 20
        # Report back every 100 generations.
        # if generation % 100 == 0:
        #     print "Generation " + str(generation)
        #     print "=" * 10
        #     for i in population:
        #         print i
        #     total = 0.0
        #     for i in fitnessScores:
        #         total += fitnessScores[i]
        #     print "Average fitness score: " + str(total / len(fitnessScores))
        
        generation += 1

    print "It took " + str(generation - 1) + " generations to get the expected output."
    print "Execution took " + str(datetime.now() - startTime)

if __name__ == "__main__":
    main()