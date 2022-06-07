'''
Los diccionarios tienen clave o key  y valor. La clave no se puede repetir
'''

diccionario = {'usuario' : 'llatzerlot' , 'password' : 123456, 'nombre' : 'Lázaro' , 'apellido' : 'Belloch' , 'edad' : 53}
print(type(diccionario))
print(diccionario) 
print(diccionario.keys())
print(diccionario.values())
print(diccionario['edad'])
diccionario['estatura'] = '175 cm'
print(diccionario) 
diccionario['apellido'] = 'Belloch Canet'
print(diccionario)

'''
Metodos de los diccionarios
'''
diccionario1 = {1:2 , 2:3 , 3:4}
diccionario2 = {4:5 , 6:7 }
print(diccionario1)
diccionario1.pop(3) #Eliminar una clave 
print(diccionario1)
diccionario1.clear() #Vacia por completo el dicconario
print(diccionario1)
diccionario1 = {1:2 , 2:3 , 3:4}
print(diccionario1)
print(diccionario1.get(2))
diccionario1.setdefault(4 , 5)
print(diccionario1)
diccionario1.update(diccionario2)
print(diccionario1)
print(diccionario2.copy())
print(diccionario2)