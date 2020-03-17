# TEAM NUMBER 91
import random

population_number = 40
secret_key = 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4'
import numpy as np
import client


def cal_pop_fitness(vector):
    # Calculating the fitness value of each solution in the current population.
    for itr in range( population_number ):
        temp = list( vector[itr][1:] )  # take each of the genes
        err = client.get_errors( secret_key, temp )
        vector[itr][0] = err[0] + err[1]  # taking fitness as the sum of the errors
    np.argsort( vector[:, 0] )


def select_mating_pool(vector, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    return vector[:num_parents, 1:]


def crossover(parents, offspring_size):
    offspring = np.empty( offspring_size )

    crossover_point = random.randrange( 1, 9 )
    for k in range( offspring_size ):
        # Index of the first parent to mate.
        parent1_idx = k % 20
        # Index of the second parent to mate.
        parent2_idx = (k + 1) % 20
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring


def mutate(val, start, stop):
    temp=val + random.uniform(start,stop)
    if (temp>10.0 or temp < -10.0)
        return mutate(val,start/2,stop/2)
    return temp

def mutation(offspring, parents, offspring_no,parents_no):
    no_of_mutations = 6 #for 11D weight vectors
    # Mutation changes a number of genes as defined by the num_mutations argument. The changes are random.

    for idx in range( offspring_no ):
        genes=random.sample(range(0,11),no_of_mutations)
        for g in genes:
            temp=mutate(offspring[idx][g],-1.0,1.0)
            offspring[idx][g]=temp

    for idx in range( parents_no ):
        genes = random.sample( range( 0, 11 ), no_of_mutations )
        for g in genes:
            temp = mutate( parents[idx][g], -1.0, 1.0 )
            parents[idx][g] = temp
    return np.append(parents,offspring,axis=0)

def initialize_population():  # load previous population as per status
    return np.loadtxt( "./saved_populations.txt", delimiter=',' )


def save_population(vector):  # saves the population that is passed in and the corresponding error rate for them
    np.savetxt( './saved_populations.txt', vector, delimiter=',' )


if __name__ == "__main__":
    vector = initialize_population()
    initial = vector

    parents = select_mating_pool( vector, 20 )
    offspring = crossover( parents, 20 )
    new=mutation(offspring,parents,20,20)
    new=np.hstack((np.zeros(40,1),new))
    cal_pop_fitness(new)

    total_population=np.append(initial,new,axis=0)
    np.argsort( total_population[:, 0] )

    final_population=total_population[:40,:] #choosing top 40
    save_population(final_population)