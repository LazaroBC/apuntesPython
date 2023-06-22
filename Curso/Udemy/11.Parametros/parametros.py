def suma(num1, num2):
    
    suma = num1 + num2
    return suma

print(suma(2,3))


# Valores globales y locales
resultado = 10
def suma(num1, num2):
    global resultado
    print(resultado)
    resultado = resultado + (num1 + num2)
    return resultado

print(suma(2,3))
print(resultado)


# Valores indefinidos

def argumento(num):
    return type(num)
n= "Hola"
print(argumento(n))
n = 10
print(argumento(n))
n = 10.5
print(argumento(n))

def argumento2(*num):
    return type(num)

print(argumento2(1,"Hola",3.2,True,5^23))
