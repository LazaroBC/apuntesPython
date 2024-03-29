#Crear un programa que permita al usuario elegir un candidato por el cual votar.
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
# Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido
# [color que corresponda al candidato elegido]”.
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles,
# indicar “Opción errónea”.

#Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula

print("Puedes votar por Pedro, Juan o Luís.\n")
candidato = input("Elige uno de los tres: \n")

if (candidato != "Pedro" and candidato != "Juan" and candidato != "Luís"):
    print("Va, prueba a elegir un que esté en la lista")
elif (candidato == "Pedro"):
    print("Usted ha votado por el partido rojo")
elif (candidato == "Juan"):
    print("Usted ha votado por el partido verde")
else:
    print("Usted ha votado por el partido rojo")