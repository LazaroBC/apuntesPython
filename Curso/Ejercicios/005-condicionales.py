'''Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''
from asyncio import FastChildWatcher


palabra1 = input("Dime una palabra: ")
palabra2 = input("Dime otra palabra y te dire si riman: ")
rima1 = (palabra1[-3:])
rima2 = (palabra2[-3:])
if rima1 == rima2 :
    print("Sí riman wey")
else :
    print("Ni pedo, no riman")
'''
Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula
'''
eleccion = input("Elige entre los candidatos A, B o C: ")
if eleccion.upper() == "A" : 
    print("Usted ha votado por el partido rojo")
elif eleccion.upper() == "B" : 
    print("Usted ha votado por el partido verde")
elif eleccion.upper() == "C" : 
    print("Usted ha votado por el partido azul") 
else :
    print("Voto nulo")
