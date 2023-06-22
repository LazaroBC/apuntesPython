
while(True):
    try:
        edad = int(input("Introduce tu edad: "))
        print("Tu edad es: " ,edad)
        break
    except:
        print("Ha ocurrido un error, introduce bien la edad")
    finally:
        print("Fin de la iteracion")


# excepciones extra

# while(True):
#     try:
#         num1 = int(input("Introduce un número: "))
#         num = 100/num1
#         print(num)
#     except ZeroDivisionError:
#         print("No se puede dividir entre 0")
# 

# while(True):
#     try:
#         edad = int(input("Introduce tu edad: "))
#         print("Tu edad es: " ,edad)
#         break
#     except ValueError:
#         print("Introduce un valor correcto")
#         break

while(True):
    try:
        edad = int(input("Introduce tu edad: "))
        print("Tu edad es: " ,edad)
        break
    except KeyboardInterrupt:
        print("Has pulsado Ctrl+C, interrumpiendo la ejecución")
        break