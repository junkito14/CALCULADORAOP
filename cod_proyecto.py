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

def get_rand_number(val_max, val_min)
    """Esta función genera números aleatorios utilizando una distribución
    uniforme para que todos tengas igual probabilidad entre dos valores
    asignados"""
    range = val_max - val_min
    elecc = random.uniform(0,1)
    return val_min + range*elecc

def first_montecarlo(num=10000):
    """Esta función realiza un montacarlo inicial, probando que funcione
    el método"""
    limite_inferior = 0
    limite_superior = 2
   
sum_ejemplos = 0
for i in range(num_ejemplos):
    x = get_rand_number(limite_inferior, limite_superior)
    sum_ejemplos += f_de_x(x)

return (limite_superior - limite inferior) * float(sum_ejemplos/num_ejemplos)
    
