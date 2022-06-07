'''
Listas.
Pueden ser homogeneas o no, o sea admiten todo tipo de datos
'''
lista = [1, 'Python', 'Nombre', 3.14, 6.28]
print(type(lista))
print(lista)
print(lista[3])
print(len(lista))
lista[0] = 0.1 # Modificar un valor de una lista
print(lista)

'''
Debanado de listas
'''
lista2 = [0,2,1,7,4,5,6,3,8,9,10]
print(lista2[5])
print(lista2[1:5]) # El último no se selecciona
print(lista2[:2])
print(lista2[4:])
print(lista2[-5])
print(lista2[-5:-2])

'''
Metodos
'''
print(lista2) 
lista2.append(11) # Append agrega al final un dato
print(lista2)

lista2.insert(3, 2.5) # Insert agrega un elemento en una determinada posición
print(lista2)
print(lista2.count(8)) 
print(lista2.index(2.5)) # Index devuelve la primera posicion que corresponde al valor indicado
lista2.sort() # Sort ordena de menor a mayo, hayq ue hacerla a parte del print
print(lista2)
lista2.reverse() 
print(lista2)


lista3 = ['Python', 24, "Lulú", "Lázaro", 12]
print(lista3[3])
lista3[3] = "Lazaro"
print(lista3[3])
# Eliminar elementos de una lista
lista3.pop() # Elimina el último elemento
print(lista3)
lista3.remove(24)
print(lista3)

'''
Llenar listas
'''
lista4 = lista3 + lista2 # Solo se pueden sumar, no confundir con la concatenación que en python es con coma
print(lista4)

lista5 = []
print(lista5)
edad = int(input("Ingresa tu edad: "))
lista5.append(edad)
print(lista5)
