#code for genetic maze solver
import random 
import math


class Individual:
    MAX_FITNESS = 100
    POSSIBLE_GENES = ["N", "E", "S", "W"]
    GENE_LENGTH = 9
    
    def __init__(self):
        self.fitness = 0
        self.genes = []
        for x in range(Individual.GENE_LENGTH):
            self.genes.append(random.choice(Individual.POSSIBLE_GENES))

    
    def Fitness(self, curLoc, endLoc, maxMag):
        x = curLoc[0] - endLoc[0]
        y = curLoc[1] - endLoc[1]
        x = x ** 2
        y = y ** 2
        mag = math.sqrt(x + y)
        fitMod = 1.0 - (mag / maxMag) 
        fitness = Individual.MAX_FITNESS * fitMod
        fitness = int(round(fitness))
        self.fitness = fitness

    def Mutate(self, index):
      self.genes[index] = random.choice(Individual.POSSIBLE_GENES)

    def CopyGenes(self, otherIndividual):
      for x in range(Individual.GENE_LENGTH):
          self.genes[x] = otherIndividual.genes[x]
      self.fitness = otherIndividual.fitness
    
    def PrintGenes(self):
      count = 0
      geneOutput = ""
      for item in self.genes:
          geneOutput += str(count) + ":" + item + " "
          count += 1
      return geneOutput

class NaturalSelection:
    def __init__(self, mutationRate):

        self.population = Population(10)
        self.mutationRate = mutationRate
        self.fittest = None
        self.secondFittest = None
        self.genCount = 0

    def MainProcess(self, maze):
        self.population.CalFitForWholePop(maze)
        print("Generation: " + str(self.genCount) + " Fittest: " + str(self.population.fittest))
        while(self.population.fittest < Individual.MAX_FITNESS and self.genCount <= 1000000):
            self.genCount += 1
            self.Selection()
            self.CrossOver()
            if random.uniform(0, 1) <= self.mutationRate:
                self.do_Mutation()

            self.AddFittestOffspring(maze)
            self.population.CalFitForWholePop(maze)
            print("Generation: " + str(self.genCount) + " Fittest: " + str(self.population.fittest) +
                  " Genes: " + self.population.Get_Fittest().PrintGenes())
        if (self.genCount > 1000000):
            print("Solution not found within 1000000 generations. Terminating program\n")
        else:
            print("Solution found in generation " + str(self.genCount))
            print("Fitness: " + str(self.population.Get_Fittest().fitness))
            print("Genes: " + self.population.Get_Fittest().PrintGenes())

    #Picks the two fittest individuals for the cross over process.
    def Selection(self):
        self.fittest = self.population.Get_Fittest()
        self.secondFittest = self.population.FindTheSecoundFittest()

    def CrossOver(self):
        crossPoint = random.randint(0, Individual.GENE_LENGTH - 1)
        for i in range(crossPoint):
            temp = self.fittest.genes[i]
            self.fittest.genes[i] = self.secondFittest.genes[i]
            self.secondFittest.genes[i] = temp

    
    def do_Mutation(self):
        mutationPoint = random.randint(0, Individual.GENE_LENGTH - 1)
        self.fittest.Mutate(mutationPoint)
        mutationPoint = random.randint(0, Individual.GENE_LENGTH - 1)
        self.secondFittest.Mutate(mutationPoint)

    def FindFittestOffspring(self):
        if self.fittest.fitness > self.secondFittest.fitness:
            return self.fittest
        return self.secondFittest

    
    def AddFittestOffspring(self, maze):
        maze.RunGenesThroughMaze(self.fittest)
        maze.RunGenesThroughMaze(self.secondFittest)
        leastFit = self.population.FindLeastFittest()
        leastFit.CopyGenes(self.FindFittestOffspring())
    
class Population:
    def __init__(self, popSize):
        self.popSize = popSize
        self.individuals = []
        self.fittest = 0
        for x in range(self.popSize):
            temp = Individual()
            self.individuals.append(temp)


    def Get_Fittest(self):
        fittestIndiv = self.individuals[0]
        for item in self.individuals:
            if(item.fitness > fittestIndiv.fitness):
                fittestIndiv = item

        self.fittest = fittestIndiv.fitness
        return fittestIndiv

    def FindTheSecoundFittest(self):
        mostFit = self.individuals[0]
        secoundMostFit = self.individuals[0]
        for item in self.individuals:
            if (item.fitness > mostFit.fitness):
                secoundMostFit = mostFit
                mostFit = item

            elif item.fitness > secoundMostFit.fitness:
                secoundMostFit = item

        return secoundMostFit

    def FindLeastFittest(self):
        leastFitIndiv = self.individuals[0]
        for item in self.individuals:
            if(item.fitness < leastFitIndiv.fitness):
                leastFitIndiv = item

        return leastFitIndiv

    def CalFitForWholePop(self, maze):
        for indiv in self.individuals:
            maze.RunGenesThroughMaze(indiv)
        self.Get_Fittest()

class Maze:
    def __init__(self):

        self.maze = [
            ["_", "_", "#", "#", "_", "#"],
            ["#", "_", "_", "#", "_", "#"],
            ["#", "#", "_", "#", "_", "E"],
            ["#", "_", "_", "_", "_", "#"],
            ["#", "_", "#", "_", "#", "#"],
            ["S", "_", "#", "_", "_", "#"]
        ]
        self.maxMag = 6.0

        self.startLocation = self.FindCharLocation("S")
        self.currentLocation = self.startLocation
        self.endLocation = self.FindCharLocation("E")

    def FindCharLocation(self, targetChar):
        for x in range(len(self.maze)):
            for y in range(len(self.maze[x])):
                if self.maze[x][y] == targetChar:
                    return [x, y]
        return None

    def PrintMaze(self):
        for x in self.maze:
            row = ""
            for y in x:
                row += y
                row += " "
            print(row)

    
    def RunGenesThroughMaze(self, individual):
        self.currentLocation = self.startLocation
        for aGene in individual.genes:
            possibleMove = None
            if aGene == "N":
                possibleMove = [self.currentLocation[0] - 1, self.currentLocation[1]]
            elif aGene == "E":
                possibleMove = [self.currentLocation[0], self.currentLocation[1] + 1]
            elif aGene == "S":
                possibleMove = [self.currentLocation[0] + 1, self.currentLocation[1]]
            elif aGene == "W":
                possibleMove = [self.currentLocation[0], self.currentLocation[1] - 1]
            else:
                print("Warning! Invalid gene detected: " + aGene)

            if self.CheckForVaildMove(possibleMove):
                self.currentLocation = possibleMove
            else:
                individual.Fitness(self.currentLocation, self.endLocation, self.maxMag)
                break

    def CheckForVaildMove(self, posibleMove):
        if (posibleMove[0] >= 0 and posibleMove[0] < len(self.maze) and
                posibleMove[1] >= 0 and posibleMove[1] < len(self.maze[0])):
            if self.maze[posibleMove[0]][posibleMove[1]] != "#":
                return True
        return False

if __name__ == "__main__":
    NS = NaturalSelection(0.05)
    aMaze = Maze()
    NS.MainProcess(aMaze)
