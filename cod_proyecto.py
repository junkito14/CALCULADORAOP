import random 

def create_numbers ():
    rng=random.Random()
    numbers = []
    for  i in range(10000-1):
        num = rng.random()
        numbers += [num]
    return numbers

print (create_numbers())
