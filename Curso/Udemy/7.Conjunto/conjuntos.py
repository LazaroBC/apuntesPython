'''
Un conjunto es una colección no ordenada de objetos únicos, o sea, no admite valores iguales, en caso de haber dos valores iguales solo considera uno Python provee este tipo de datos «por defecto» al igual que otras colecciones más convencionales como las listas, tuplas y diccionarios.

Los conjuntos son ampliamente utilizados en lógica y matemática, y desde el lenguaje podemos sacar provecho de sus propiedades para crear código más eficiente y legible en menos tiempo.
'''
conjunto1 = {1, 2, 3, 4, 5, 5}
conjunto2 = set([6,7,8,9])
conjunto3 = set((10,11,12))
print(type(conjunto1))
print(conjunto1)
print(type(conjunto2))
print(conjunto2)
print(type(conjunto3))
print(conjunto3)

'''
Métodos
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''

conjunto1.add(6)
print(conjunto1)
conjunto1.remove(5) # conjunto1.discard(5) 
print(conjunto1)
conjunto1.pop() # Elimina  el primer valor
print(conjunto1)
conjunto1.update([6,7,8,9,10,1,5])
print(conjunto1)