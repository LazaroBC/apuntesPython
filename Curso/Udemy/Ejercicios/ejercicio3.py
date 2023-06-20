# Escribir un programa que diga si dos palabras riman,
# de modo que si son iguales las tres ultimas letras diga riman
# si son iguales solo las dos ultimas rimpa poco. El resto no rima

palabra1 = input("Ingresa la primera palabra: \n")
palabra2 = input("Ingresa la segunda palabra: \n")


if (len(palabra1) < 3 or len(palabra2) < 3):
    print("No riman, prueba a poner palabras de más de tres letras")
elif (palabra1[-3] == palabra2[-3]):
    print("¡¡¡¡¡¡¡RIMAN!!!!!!")
elif (palabra1[-2] == palabra2[-2]):
    print("!!Riman Poco¡¡")
else :
    print("No riman")