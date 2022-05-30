'''
Ejercicio 1
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''

from math import sqrt

print('Dime los valores que necesitas para resolver la ecuación\n')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
x1 = 0
x2 = 0
if ((b**2)-(4*a*c)) < 0:
    print('No se puede realizar la operación porque la raiz cuadrada es de un número negativo')
else:
    x1 = (-b + sqrt(((b**2)-(4*a*c))))/(2*a)
    x2 = (-b - sqrt(((b**2)-(4*a*c))))/(2*a)
print('El resultado es: ', '\nx1= ', x1, '\nx2= ', x2)

'''
Ejercicio 2
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final
'''
alumno = input('Nombre del alumno: ')
p1 = float(input('Práctica 1: '))
p2 = float(input('Práctica 2: '))
p3 = float(input('Práctica 3: '))
ep = float(input('Exámen parcial: '))
ef = float(input('Exámen final: '))
pp = (p1+p2+p3) / 3
prom = (pp + 2*ep +3*ef) / 6
print('El promedio de ', alumno, ' ha sido de ', prom, '.')

'''
Ejercicio 1
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
'''
import time
vocal = input('Necesito una vocal en minúscula: ')
vocal = vocal.lower()
print(vocal)
consonante = input('Necesito una consonante en mayúscula: ')
consonante = consonante.upper()
print(consonante)
print('Convirtiendo...')
time.sleep(5)
vocalMayuscula = vocal.upper()
print(vocalMayuscula)
consonanteMinuscula = consonante.lower()
print(consonanteMinuscula)
print('Concatenando...')
time.sleep(5)
print(vocalMayuscula + consonanteMinuscula)

'''
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
'''
import time
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
sexo = input("¿Cuá es tu sexo? ")
print("Deduciendo...")
time.sleep(2)
print("Te llamas ", nombre) 
print("Tu edad es de ", edad, "años ") 
print("Tu sexo es ", sexo) 

print("Te llamas {}".format(nombre)) 
print("Tu edad es de {}".format(edad), "años ") 
print("Tu sexo es {}".format(sexo)) 

