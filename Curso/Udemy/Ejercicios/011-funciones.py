# Ejercicio 1

# Crear un programa que tenga una lista, 
# luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. 
# Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

def pedir_numeros():
    lista = []
    n = int(input("Ingrese la cantidad de números que desea agregar a la lista: "))
    
    for _ in range(n):
        numero = int(input("Ingrese un número: "))
        lista.append(numero)
    
    return lista

def ordenar_pares_impares(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

# Pedir números al usuario y agregarlos a la lista
numeros_lista = pedir_numeros()

# Ordenar los números pares e impares en listas separadas
pares, impares = ordenar_pares_impares(numeros_lista)

# Imprimir los resultados
print("Números pares:", pares)
print("Números impares:", impares)
# Ejercicio 2

# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
    resultado = 1

    # Verificar si el número es mayor que 1
    if numero > 1:
        # Calcular el factorial
        for i in range(2, numero + 1):
            resultado *= i

    return resultado

# Ejemplo de uso de la función
numero = int(input("Ingrese un número entero positivo: "))
factorial_numero = factorial(numero)
print("El factorial de", numero, "es:", factorial_numero)
