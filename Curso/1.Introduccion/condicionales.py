edad = float(input("Dime tú edad: "))
if edad <= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

'''
Elif
'''
letra = input("Introduce una vocal: ")

if letra.lower() == "a" :
    print("Tu vocal es una a")
elif letra.lower() == "e" :
    print("Tu vocal es una e")
elif letra.lower() == "i" :
    print("Tu vocal es una i")
elif letra.lower() == "o" :
    print("Tu vocal es una o")
elif letra.lower() == "u" :
    print("Tu vocal es una u")
else :
    print("Te dije una vocal")

'''
Condicionales anidados
'''

nombre = input("Usuario: " )
contrasena = str(input("Contraseña: "))

if nombre == "Juan":
    if contrasena != ("123456"): 
        print("Eres Juan pero tu contraseña no es ", contrasena)
    else:
        print("Puedes pasar")
else:
    print("No te sabes ni tu usuario ni tu contraseña")