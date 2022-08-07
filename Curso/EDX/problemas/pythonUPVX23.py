#contar elementos de una lista
lista = [9,13,2,7,124,-5]
print(len(lista))
#Cómo lo harías sin la función len?
#TU RESPUESTA AQUÍ
cuenta = 0
for i in lista:
    cuenta = cuenta + 1
print (f'Hay  {cuenta} elementos')

#suma los valores de los elementos
lista = [9,13,2,7,124,-5]
print(sum(lista))
#Cómo lo harías sin la función sum?
suma = 0
for i in lista:
    suma = suma + i
print(f'La suma es efectivamente {suma}')

#calcula la media de los valores de los elementos
lista = [9,13,2,7,124,-5]
print(sum(lista)/len(lista))
#Cómo lo harias sin sum ni len?
cuenta = 0
suma = 0
for i in lista:
    cuenta = cuenta +1
    suma = suma + i
print(f'La media es {suma/cuenta}')

#y si quisieras la media de los valores positivos de los elementos?
cuenta = 0
suma = 0
for i in lista:
    if (i > 0):
        cuenta = cuenta +1
        suma = suma + i
        print(f'suma parcial es: {suma}')
        print(f'conteo parcial es: {cuenta}')
print(f'La media delos números positivos es {suma/cuenta}')

#y si quisieras la media de los valores absolutos de los elementos?
suma = 0
cuenta = 0
print(f'valor inicial es :{suma}')
for elemento in lista:
  suma = suma + abs(elemento)
  cuenta = cuenta + 1
  print(f'suma parcial es: {suma}')
  print(f'conteo parcial es: {cuenta}')
print(f'la media de los elementos es: {suma/cuenta}')

#Buscando si un elemento existe
lista = [9,13,2,7,124,-5]
print(7 in lista)
#como lo harías sin usar in?
#TU RESPUESTA AQUÍ
for i in lista:
    if i == 7:
        print (i)

existe = False
elementoBuscado = 7
for item in lista:  
  if item == elementoBuscado:
    existe = True    
    break
if existe==True:
  print(f"El elemento {elementoBuscado} esta en la lista")
else:
  print(f"No hemos podido encontrar {elementoBuscado} en la lista")

#Buscando el elemento más grande/pequeño de la lista
lista = [9,13,2,7,124,-5]
print(max(lista))
print(min(lista))
#como lo harías sin usar max/min?
#TU RESPUESTA AQUÍ
#Esta solución no es valida ya que en caso de ser todos lo valores negativos nos daría como valor mayor el 0
'''
maximo = 0
minimo = 0
for i in lista:
  if i > maximo:
    maximo = i
  elif i < minimo:
    minimo = i
print(f'El número más alto es {maximo}')
print(f'El número más pequeño es {minimo}')
'''
mayor = None
menor = None
for i in lista:
  if mayor == None or menor == None:
    mayor = i
    menor = i
  else:
    if mayor < i:
      mayor = i
    if menor > i:
      menor = i
print(f'El número más alto es {mayor}')
print(f'El número más pequeño es {menor}')