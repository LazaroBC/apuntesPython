print(2 + 2)
print(2 - 2)
print(10 * 10)
print(17 / 5)
print(3 ** 2)
print(17 // 5)
print(17 % 9) #Módulo
print(9 % 9) #Módulo

# Variables aritméticas

num1 = 10
num2 = 5

print(num1,num2)
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
print(num1//num2)
print(num1%num2)

suma = num1 + num2

# Jerarquía de operaciones
num3 = 100
num4 = 50
num5 = 25
num6 = 10
print (num3 + num4 * num5) # En este caso primero ejecuta la multipicación y luego la suma
print ((num3 + num4) * num5) # En este caso primero realiza la operación dentro de los parentesis
print ((num3 + num4) * num5 - num6) # En este caso primero realiza la operación dentro de los parentesis y luego sigue el orden lógico
print ((num3 + num4) * (num5 - num6)) # En este caso realiza primero los parentesis y luego la multiplicación
''' En ese cas daría error al dividir or cero
print ((num3 + num4) * (num5 - num6) / (num1 - num1))''' 
