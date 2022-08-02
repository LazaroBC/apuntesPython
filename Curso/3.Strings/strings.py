'''
Strings literales o como escapar caracteres
'''
cadena = "Esto es un ejemplo de cadena de texto"
print (cadena)
cadena = "Esto es un \"ejemplo\" de cadena de texto"
print (cadena)
cadena = "Esto es un \nejemplo de cadena de texto"
print (cadena)
cadena = "Esto es un \tejemplo de cadena de texto"
print (cadena)
cadena = "Esto es un \bejemplo de cadena de texto"
print (cadena)
cadena = "Esto es un \fejemplo de cadena de texto"
print (cadena)
cadena = "Esto es un \rejemplo de cadena de texto"
print (cadena)
cadena = "Esto es un \vejemplo de cadena de texto"
print (cadena)
cadena = "Esto es un \aejemplo de cadena de texto"
print (cadena)
'''
Convertir un número a string
'''

cadena1 = "Hola pibe"
cadena2 = " o piba"
numero = 1
print(cadena1 + cadena2) # Concatenación o suma
print(numero,  "Hola " , cadena2)

print(cadena2 * 5) # Multiplicador

'''
Función STR
'''

print(type(numero))
print(type(str(numero)))

'''
SubStrings
Devanado de cadenas
'''
print(len(cadena))
print(cadena)
print(cadena[2]) # el primer caracter es el de orden 0
print(cadena[0:10]) # Devanado
print(cadena[:10])
print(cadena[3:10])
print(cadena[3:])
print(cadena[-4: -1])

'''
Metodos de cadenas
'''
cadena = "    esto es un Ejemplo de cadena de texto Python@    " 
cadena5 = "LazaroBelloch5"
print(cadena.lower()) # Minúsculas
print(cadena.upper()) # Mayúsculas
print(cadena.capitalize()) #Primera letra en mayúsculas, solo la primera
print(cadena.title()) # Primera letra de cada palabra en mayúsculas
print(cadena.swapcase()) # Cambia minúsculas por mayúsculas y viceversa
print(cadena.count("to")) # Suma la cantidad de to que hay en la cadena
print(cadena.isalnum()) # Devuelve false si la cadena contiene carácteres no alfanuméricos
print(cadena5.isalnum()) # Devuelve true si la cadena contiene solo carácteres alfanuméricos
print(cadena.isalpha()) # Devuelve true si todos los carácteres son alfabeticos
print(cadena.strip()) # Elimina los espacios al principio y al final
print(cadena5.zfill(20)) # Agrega ceros a la izquierda hasta completar el numero indicado de carácteres
s = "; ".join(["1", "2", "3"])
print(s)
s = "Python,Java,C"
print(s.split(",")) #['Python', 'Java', 'C']
print(cadena.strip().split(" "))