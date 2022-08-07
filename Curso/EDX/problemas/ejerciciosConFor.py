'''
Acá encontrarás ejercicios para practicar la estructura de control de bucle o repetición fija (for).

En los siguientes videos podrás ver una explicación de la estructura y también la resolución paso a paso de estos ejercicios:

Repetición fija: for
Ejercicios con la estructura de repetición fija
Ejercicio con la estructura de repetición fija
Ejercicios con break y continue
La resolución de cada ejercicio se muestra al hacer click sobre la consigna.

Nota: estos enunciados y resoluciones fueron diseñados con el objetivo de ayudar a programadores principiantes a desarrollar habilidades algorítmicas y de razonamiento lógico. La finalidad principal no se enfoca en la sintaxis y herramientas concretas de Python 3, y la mayoría de los ejercicios podrían resolverse con cualquier lenguaje dentro del paradigma imperativo. Es por ese motivo que algunas resoluciones muestran un algoritmo genérico y no orientado específicamente a Python.

1
Imprimir todos los dígitos decimales, del 0 al 9, utilizando una repetición.
'''
#for i in range(0,10):
#    print(i)
'''
2
Imprimir todos los números entre el 100 y el 199.
'''
#for i in range(100,200):
#    print(i)
'''
3
Imprimir los números entre el 5 y el 20, saltando de tres en tres.
'''
#cont = 2
#for i in range(5,21):
#    cont = cont + 1
#    if cont%3 == 0:
#        print(i)
'''
4
Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos 
entre el ingresado por el usuario y uno menos del doble del mismo.
'''
#num = int(input(f'Ingresa un entero positivo: '))
#num2 = (num*2)
#for i in range(num,num2):
#    print(i)
'''
5
Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. 
En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados.
'''
#num1 = int(input(f'Ingresa un número: '))
#num2 = None
#for i in range(0,num1):
#    num2 = int(input(f'Ingresa número a sumar: '))
#    num1 = num1 + num2
#    print(f'La suma parcial es: {num1}')
#print(f'La uma es total: {num1}')

'''
6
Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales 
que aparecen en esa frase (sin repetirlas).
'''
#frase = input(f'Dime una frase bonita: ')
#vocales = ''
#for i in frase:
#    if i.lower() in 'aeiou':
#        vocales = vocales + i.lower()
#        
#resultado = set(vocales)
#print(f'Las vocales que he encontrado son: ' + ', '.join(resultado))

'''
7
Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.
'''
#frase = input(f'Escribe algo: ')
#cantidad = 0
#for i in frase:
#    if i.lower() in 'aeiou':
#        cantidad = cantidad +1
#print(f'Lo que has escrito contiene {cantidad} de vocales')
'''
8
Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.
'''
#sumatoria = 0
#for i in range(0,101):
#    sumatoria = sumatoria + i
#print(sumatoria)

'''
9
Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.
'''
sumatoria = 0
for i in range(0,101):
    if i%3 == 0:
        sumatoria = sumatoria + i
print(sumatoria)

'''
10
Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
'''

'''
11
Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
'''
'''
12
Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
'''
'''
13
Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
'''
'''
14
Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
'''
