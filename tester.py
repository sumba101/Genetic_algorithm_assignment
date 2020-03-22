# TEAM NUMBER 91
import random
import re

overweight_error = 3.705362469604573213e+06
population_number = 6
secret_key = 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4'
import numpy as np
import client


def cal_pop_fitness(vector):
    # Calculating the fitness value of each solution in the current population.
    for itr in range( population_number ):
        temp = list( vector[itr][1:] )  # take each of the genes

        err = client.get_errors( secret_key, temp )
        vector[itr][0] = 0.5 * err[0] + 1.2 * err[1]  # taking fitness as the sum of the errors
        print( "query number:- ", itr, vector[itr][0] )


def select_mating_pool(vector, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    return vector[:num_parents, 1:]


def crossover(parents, offspring_size):
    offspring = np.empty( (offspring_size, 11) )

    crossover_point = 5

    for k in range( offspring_size ):
        # Index of the first parent to mate.
        parent1_idx = k % 3
        # Index of the second parent to mate.
        parent2_idx = (k + 1) % 3

        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring


def mutate(val, start, stop):
    temp = val + random.uniform( start, stop )
    if (temp > 10.0):
        return mutate( val, start, 10 - val )
    if temp < -10.0:
        return mutate( val, -10 - val, stop )
    return temp


def mutation(offspring, parents, offspring_no, parents_no):
    for idx in range( offspring_no ):
        for g in range( 0, 11 ):
            temp = mutate( offspring[idx][g], -1.0, 1.0 )
            offspring[idx][g] = temp

    for idx in range( parents_no ):
        for g in range( 0, 11 ):
            temp = mutate( parents[idx][g], -1.0, 1.0 )
            parents[idx][g] = temp
    return np.append( parents, offspring, axis=0 )


def initialize_population():  # load previous population as per status
    # returnable = np.loadtxt( "./saved_populations.txt", delimiter=',' )
    returnable = np.loadtxt( "./saved_populations.txt", delimiter=',' )

    np.savetxt( './temp.txt', returnable, delimiter=',' )
    return returnable


if __name__ == "__main__":
    # vector = initialize_population()
    # print( "Population has been loaded" )
    #
    # parents = select_mating_pool( vector, 3 )
    # offspring = crossover( parents, 3 )
    #
    # np.savetxt( './parents.txt', parents, delimiter=',' )
    # np.savetxt( './offspring.txt', offspring, delimiter=',' )
    #
    # temp = mutation( offspring, parents, 3, 3 )
    # print( "New population has been created" )
    #
    # np.savetxt( './mutated_offspring.txt', temp, delimiter=',' )
    #
    # new = np.append( np.zeros( (6, 1) ), temp, axis=1 )
    # print( "starting fitness measure now" )
    #
    # cal_pop_fitness( new )
    # print( "fitness measured" )

    # np.savetxt( './evaluated_population.txt', new, delimiter=',' )


    total_population = np.loadtxt( "./saved_populations.txt", delimiter=',' )

    total_population = total_population[total_population[:, 0].argsort()]
    np.savetxt( './saved_populations.txt', total_population, delimiter=',' )
