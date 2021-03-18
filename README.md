# CS441-Ai-Final-Group-Project
CS441/541 Artificial Intelligence: A Maze Solver

Developers: Charlene Namuyige, Leah Moser, Natasha Needham, Salem Alathari, Sam Rind 

# Brief Description
A maze is a network of paths designed as a puzzle where an agent would need to find the specific path that leads to the exit. This maze solver is intended to find a route from start to finish in this maze. 
There exists a number of algorithms that can generate and solve a maze solver in artificial intelligence. 

# Genetic Algorithm 
A genetic algorithm is a search heuristic that is inspired by Charles Darwin's theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation. 
* Initial Population: Starts with a set of individuals known as the population.This population is a fixed size 10. An individual is characterized by a set of variables known as the genes. Genes have a set  gene_length 9 and the possible genes are: [N, S, E, W] 
* Fitness function: The fitness function determines the ability of an individual to compete with other individuals. A fitness score is given to each individual and the probability that an individual is selected for reproduction is based on its fitness score. 
* Selection: The selection phase is to select the fittest individuals and let them pass their genes on to the next generation. Individuals with the highest fitness scores tend to be selected for reproduction.  
* Crossover: Crossover is the phase of the genetic algorithm where for each pair of the parents to be mated, a crossover point is chosen at random from within the genes. 
* Mutation: During reproduction, some of the genes might be subjected to a mutation with low random probability. Mutation occurs to prevent premature convergence. 

# How to run program 
  To run this program, simply compile and run in a python environment. 
  
# RL Algorithm
Our reinforcement learning algorithm initially has all actions at a value of zero. As the training goes on, the value for a given move is updated based on the reward gained after it occurred. Training ends after a fixed number of mazes, or if a 100% win rate is achieved. The algorithm explores the maze less as training goes on in order to narrow down a path to the exit. The maze is set, but the starting point is random. 

# How to run the RL program
