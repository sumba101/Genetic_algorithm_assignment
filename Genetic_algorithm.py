# TEAM NUMBER 91
import random

overweight_error=3.705362469604573213e+06
population_number = 40
secret_key = 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4'
import numpy as np
import client


def cal_pop_fitness(vector):
    # Calculating the fitness value of each solution in the current population.
    for itr in range( population_number ):
        temp = list( vector[itr][1:] )  # take each of the genes
        
        err = client.get_errors( secret_key, temp )
        vector[itr][0] = 0.5*err[0] + 1.2*err[1]  # taking fitness as the sum of the errors
        print("query number:- ",itr, vector[itr][0])
    np.argsort( vector[:, 0] )


def select_mating_pool(vector, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    return vector[:num_parents, 1:]


def crossover(parents, offspring_size):
    offspring = np.empty( (offspring_size,11) )

    crossover_point = random.randrange( 1, 9 )

    breakpoint="here"

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
    if (temp>10.0):
        return mutate(val,start,10-val)
    if temp < -10.0:
        return mutate(val,-10-val,stop)
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

def generation():
    overweight=[0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883,
                                          8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07,
                                          3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
    err = client.get_errors( secret_key, overweight )
    sum=err[1]
    overweight.insert(0,sum)
    page = np.empty( (40, 12) )
    for itr in range(40):
        for ind,x in enumerate(overweight):
            page[itr][ind]=x
    save_population(page)

if __name__ == "__main__":
    vector = initialize_population()
    initial = vector
    print("Population has been loaded")
    parents = select_mating_pool( vector, 20 )
    offspring = crossover( parents, 20 )
    temp=mutation(offspring,parents,20,20)
    print("New population has been created")
    new=np.append(np.zeros((40,1)),temp,axis=1)
    print("starting fitness measure now")
    cal_pop_fitness(new)
    print("fitness measured")
    total_population=np.append(initial,new,axis=0)
    np.argsort( total_population[:, 0] )
    #save_population(total_population)
    
    final_population=total_population[:40,:] #choosing top 40
    save_population(final_population)
    print("population has been saved")
    generation()
