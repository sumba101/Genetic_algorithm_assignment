import numpy as np

import client

secret_key = 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4'


def select_mating_pool(vector, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    return vector[:num_parents, 1:]


def initialize_population():  # load previous population as per status
    returnable = np.loadtxt( "./safety.txt", delimiter=',' )
    return returnable


def get_past_submissions():
    return np.loadtxt( "./submitted_vectors.txt", delimiter=',' )


vector = initialize_population()
current = select_mating_pool( vector, 40 )

past = get_past_submissions()
print( "Population has been loaded" )

print( "processing the population" )
finished = set()
for w in past:
    finished.add( tuple( w ) )
submission_set = list()
for w in current:
    temp = tuple( w )
    if temp not in finished:
        submission_set.append( w )

print( "finished processing" )
print( "New weight vectors = ", len( submission_set ) )

op = input( "would you like to submit it?, y/n :- " )
if (op == 'y'):
    for itr in submission_set:
        temp = list( itr )  # take each of the genes
        # submit_status = client.submit( secret_key, temp )
        # print( "query status:- ", submit_status )
        past = np.append( past, [np.asarray( temp )], axis=0 )
    # now putting the finished vectors into submitted vectors.txt
    np.savetxt( './submitted_vectors.txt', past, delimiter=',' )
