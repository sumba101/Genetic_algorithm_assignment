import client
#team number 91

#population of 40

with open('./overfit_weights.txt','r') as f:
    overfit=f.read().split('[')
    overfit=overfit[1].split(']')
    vector=[float (n) for n in overfit[0].split(',')]

err = client.get_errors( 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4', vector )
print(err)