'''Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
'''
lista = [20, 50, "Curso", 'Python', 3.14]
print("Estos son los valores ", lista)
dato1 = input("Dame el primer dato: ")
dato2 = input("Dame el segundo dato: ")
lista[0] = dato1
lista[1] = dato2
print(lista)
lista.insert(0, dato1)
lista.insert(1, dato2)
print(lista)
'''
Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos
'''
lista2 = [1,2,3,4,5,6,7,8,9,10]
print(lista2)
lista2[3] = lista2[3]*2 # lista2[3] *= 2
lista2[6] = lista2[6]*2
lista2[8] = lista2[8]*2
print(lista2)
