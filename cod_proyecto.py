import random 
import math
import numpy as np

def create_numbers ():
    """ Esta función sirve para generar números aleatorios entre 0 y 1""" 
    rng=random.Random()
    numbers = []
    for  i in range(10000-1):
        num = rng.random()
        numbers += [num]
    return numbers

print (create_numbers())
