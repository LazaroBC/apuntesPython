# Ejercicio 1

# Crear un programa que tenga dos funciones, 
# una que contenga el area de un cuadrado con argumentos de base y altura; 
# y la otra el area de un circulo con argumento de radio

import math
def areaCuadrado(base, altura):
    area = base * altura
    return area

def areaCirculo(radio):
    
    return pow(radio,2) * math.pi

print(areaCuadrado(2,3))
print(areaCirculo(3))

# Ejercicio 2

#Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

def medida(*lista):
    return len(lista)

print(medida([1,2,3,4,5,6,7,8,9,10],1,2,3,4,5,6,7,8,9,10))

