#code for genetic maze solver
import random 
import math


class Individual:
    MAX_FITNESS = 100
    POSSIBLE_GENES = ["N", "E", "S", "W"]
    GENE_LENGTH = 9
    
    def __init__(self):
        self.fitness = 0
        self.gene = []
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