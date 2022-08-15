'''1
Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números ingresados.
'''
# suma = 0
# i = 1
# while i !=0:
#     i = int(input(f'Voy a sumar números hasta que introduzcas un 0: '))
#     suma= suma +i
#     if i == 0:
#         print('Hemos terminado')
# print(f'El sumatorio de tus números es: {suma}')
    
'''2
Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
'''
# suma = 0
# i = 1
# while i !=0:
#     i = int(input(f'Voy a sumar números hasta que introduzcas un 0: '))
#     if i > 0:
#         suma= suma +i
#     if i == 0:
#         print('Hemos terminado')
# print(f'El sumatorio de tus números es: {suma}')
'''3
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
'''
# mayor = 0
# menor = 0
# salida = 0
# i = 1
# while i !=0:
#     i = int(input(f'Voy a comparar números hasta que introduzcas un 0: '))
#     if i > 0:
#         mayor = i
#         if mayor > menor:
#             print(menor, mayor, salida)
#             salida = mayor
#             print(menor, mayor, salida)
#             menor = mayor
#             print(menor, mayor, salida)
#     if i == 0:
#         print('Hemos terminado')
# print(f'El mayor de tus números es: {salida}')
'''4
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
'''
# suma = 0
# i = 1
# while i !=0:
#     i = int(input(f'Voy a sumar los números positivos hasta que introduzcas un 0: '))
#     if i > 0:
#         suma= suma +i
#     if i == 0:
#         print('Hemos terminado')
# print(f'El sumatorio de tus números es: {suma}')
'''5
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. 
Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
'''
# cantPares = 0
# suma = 0
# i = 0
# while i != -1:
#     i = int(input(f'Introduce números psoitivos hasta que introduzcas un -1: '))
#     if i != -1:
#         print(f'el número suma: {sum(int(digit) for digit in str(i))}')
#     if i%2 == 0:
#         cantPares = cantPares +1
# print(f'El total de números pares introducidos es: {cantPares}')
'''6
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, 
informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú 
y el programa finalizará.
'''

# print(f'Menú\n\
# ----\n\
#     1.-Comenzar programa\n\
#     2.-Imprimir listado\n\
#     3.-Finalizar programa')
# opcion = int(input('Seleciona una opción: '))
# while opcion != 1 or opcion != 2 or opcion != 3:
#     print(f'Elige una opción correcta')
#     if opcion == 1:
#         print(f'Comenzando el programa')
#     elif opcion == 2:
#         print(f'Imprimiendo el listado')
#     elif opcion == 3:
#         print('Finalizando el programa')
#         break
#     opcion = int(input('Seleciona una opción: '))
# print(f'Adios')
'''7
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
'''
# frase = input(f'Dime una frase que contenga la letra l\n').lower()
# letra = 'l'
# indice = 0
# while letra == 'l':
#     if frase[indice]=='l':
#         print(f'La l a aparecido por primera vez en la posición {indice+1}')
        
#         break
#     print(f'No hubo coincidencia en la posicion {indice+1}')
#     indice = indice +1
'''8
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. 
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
se le debe aplicar un 10% de descuento.
'''
# monto = None
# cantidad = 0
# negativos = 0
# while monto != 0:
#     monto = float(input(f'Introducir cantidad (0 para terminar):\n'))
#     if monto > 0:
#         cantidad = cantidad + monto 
#         print(cantidad)
#     else:
#         negativos = negativos +1
# if cantidad >= 1000:
#     cantidad = cantidad * 0.90
#     print(f'Aplicado descuento 10%: {cantidad}')
# else: 
#     print(f'Monto total = {cantidad}')
# print(f'Cantidades descartadas: {negativos}')
'''9
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
'''
# from curses.ascii import isdigit

# numeros = ''
# par = 0
# impar = 0
# ceros = 0
# digito = None
# negaFloat = int
# while numeros != '0' :
#     numeros = input(f'Introduce un número entero positivo: ')
    
#     if numeros == '0':
#         break
#     for i in numeros:
#         if numeros.isdigit() == False or int(numeros) < 0:
#             print(f'No valida')
#         else:
#             if int(i) == 0:
#                 ceros = ceros +1
#             elif int(i)%2 == 0:
#                 par = par +1
#             else:
#                 impar = impar +1
# print(f'Dígitos pares: {par}')
# print(f'Dígitos impares: {impar}')
# print(f'Ceros: {ceros}')
'''10
Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 
que contenga sólo una barra (“/”) se considera que termina una línea.Por cada línea completa, 
informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). 
Finalmente, informar cuántas líneas completas se ingresaron. 
**Ejemplo de ejecución:** 
Libro: Los 3 mosqueteros 
Libro: Historia de 2 ciudades 
Libro: / 
Línea completa. Aparecen 2 dígitos numéricos. 
Libro: 20000 leguas de viaje submarino 
Libro: El señor de los anillos 
Libro: / 
Línea completa. Aparecen 5 dígitos numéricos. 
Libro: 20 años después 
Libro: * 
Fin. Se leyeron 2 líneas completas.
'''
# cadena = ''
# digitos = 0
# lineas = 0
# while cadena != '*':
#     cadena = input(f'Dime el título de un libro: ')
#     print(f'Libro: {cadena}')
#     for i in cadena:
#         if i.isdigit() == True:
#             digitos = digitos + 1
#     if cadena == '/':
#         print(f'Linea completa: Aparecen {digitos} digitos numéricos')
#         digitos = 0
#         lineas = lineas +1
# print(f'Fin. Se leyeron {lineas} lineas completas')
'''11
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
'''
'''12
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, 
mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), 
ya sea uno o más.
'''