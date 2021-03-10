#code for genetic maze solver
import random 
import math

MAX_FITNESS = 100
POSSIBLE_GENES = ["N", "E", "S", "W"]
GENE_LENGTH = 9

class Individual:

    def __init__(self):
        self.fitness = 0
        self.gene = []
        for x in range(Individual.GENE_LENGTH):
            self.genes.append(random.choice(Individual.POSSIBLE_GENES)))