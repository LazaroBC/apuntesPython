# <nombre de la variable> = <valor>
nombre  = "Lázaro"
apellido = "Belloch"
numero = 69
flotante = 3.14
print(type(nombre))
print(nombre + " " + apellido)
print(type(numero))
print(numero)
print(type(flotante))
print(flotante)

# Consejos sobre variables
# No se pueden usar nomres de variables reservados el comando para ver las palabras reservadas es:
import keyword
print("Palabras reservadas: ") 
print(keyword.kwlist)
# Las variables no pueden empezar por un número
# No se pueden usas carácteres especiales @~{-\}
# No pueden llevar espacios
# Colocar variables descriptivas
# Utilizar caracter camello  o serpiente 
hombreJoven = 1
MujerJoven = 1

'''Declarar una constante, ya que en python no existen las constantes. 
Para ello la convencion es declarar la variable en mayúscula Python no la reconoce como constante, 
pero entre programadores identifica'''
PI = 3.14

# Declarar variables en una sola sentencia
nombre, apellido , edad = "Lázaro" , "Belloch" , 53
print(nombre)
print(apellido)
print(edad)

'''Tipos de datos:
Números enteros y flotantes'''
num1 = 40
num2 = 3.673
print(type(num1))

'''Función float'''
print(type(float(num1)))
print(float(num1))

print(type(num2))

'''Funcion int (esta función noo reedondea, solo quita los decimales)'''
print(type(int(num2)))
print(int(num2))

''' Operadores Aritméticos
+ - * / 

Módulo toma en cuenta el resto de una división

Exponenciación
**

División entera
//

Jerarquía, orden en la que se realizan las operaciones
1.- Parentesis
2.- Exponenciación
3.- Multiplicación o división
4.- Sumas y restas


'''