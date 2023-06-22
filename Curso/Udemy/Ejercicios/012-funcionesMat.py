# Librerías matemáticas
# NumPy
# SciPy
# SymPy
# Matplotlib
# Pandas
# Statsmodels
# Scikit-learn
# Keras

import math, random
print(math.sqrt(25))
print(math.pi)
print(math.e)
print(math.sin(0))
print(math.cos(0))
print(math.tan(0))
print(math.degrees(0))
print(math.radians(0))
print(math.pow(math.pi,2))
print(math.exp(1))
print(math.log(2.718281828459045))
print(math.log10(10))
print(math.log2(2))
print(math.factorial(5))
print(random.randint(1,100))

def asignacion():
    return 1,2,3,4,5
lista = []
lista = asignacion()
print(lista)

# Ejercicio 1

# Crear una funcion que pida dos numeros. 
# Si el primero es mayor al segundo, el programa debe retornar el valor 1; 
# si el segundo es mayor al primero, debe retornar -1; 
# si ambos son iguales, debe retornar 0
def mayor_menor():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0
print(mayor_menor())


# Ejercicio 2

# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def factura():
    cantidad = float(input("Ingrese el monto de la factura: "))
    iva = float(input("Ingrese el porcentaje de IVA: "))
    if iva == 0:
        iva = 21
    return cantidad + (cantidad * (iva/100))
print(factura())


