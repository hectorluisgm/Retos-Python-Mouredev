
#  * Enunciado: Crea una función que retorne el número total de bumeranes de 
#  * un array de números enteros e imprima cada uno de ellos.
#  * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
#  *   seguidos, en el que el primero y el último son iguales, y el segundo
#  *   es diferente. Por ejemplo [2, 1, 2].
#  * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] 
#  *   y [4, 2, 4]).


import random
from module import BoomerangFunction


my_list = [2, 1, 2, 3, 3, 4, 2, 4]

BoomerangFunction(my_list)

elemento = 0
my_random_list = []


while elemento < 100:
    a = random.randint(1,9)
    my_random_list.insert(elemento,a)
    elemento += 1

print(my_random_list)

# BoomerangFunction(my_random_list)



