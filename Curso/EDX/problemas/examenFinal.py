'''
Cargar el fichero "Quijote.txt" del ejercicio del tema 7 con el código de caracteres correcto, crear una función que permita seleccionar el número de párrafo que se solicita más abajo (empezando a contar por 0 para el primer párrafo) como en el ejercicio del tema 7 y le aplique a ese párrafo una encriptación por desplazamiento de código (como la explicada en el tema 6) con el desplazamiento positivo indicado más abajo, devolviendo el párrafo encriptado y obteniendo a la vez el valor numérico del código del caracter que se encuentra en la posición del párrafo que se indica más abajo (empezando a contar por 0 para el primer caracter del párrafo). Guardar el párrafo encriptado en una variable y crear una función a la que pasarle el párrafo encriptado y el desplazamiento aplicado y que permita desencriptar el texto aplicando el mismo desplazamiento de código en sentido inverso (esta parte no se evalua).
Número de párrafo: 1
Desplazamiento del código de encriptación: 8
Número de carácter dentro del párrafo: 321
'''
# def primeraFrase(parrafo):
#     #primero cargamos el fichero
#     fichero = open("quijote.txt")
#     #lo leemos
#     texto = fichero.read()
#     #y seleccionamos el párrafo indicado en el parámetro 
#     parrafos = texto.split('\n')
#     #eliminamos los párrafos vacios tras el split 
#     while '' in parrafos: 
#         parrafos.remove('')      
#         parrafoSeleccionado=parrafos[parrafo]
#      #devolvemos el parrafo a encriptar
#     return parrafoSeleccionado
# primeraFrase(1)
# def primerafrase(parrafo):
#     #primero cargamos el fichero
#     fichero = open('quijote.txt')
#     #lo leemos
#     texto = fichero.read()
#     #y seleccionamos el párrafo indicado en el parámetro 
#     parrafos = texto.split('\n')
#     #eliminamos los párrafos vacios tras el split 
#     while '' in parrafos: 
#         parrafos.remove('')    
#     parrafoseleccionado=parrafos[parrafo]
#     #vamos a buscar donde acabaría la primera frase buscamos los delimitadores que nos han pedido 
#     #y añadimos sus posiciones a una lista
#     delimitadores =[]
#     delimitadores.append(parrafoseleccionado.find(','))
#     delimitadores.append(parrafoseleccionado.find('.'))
#     delimitadores.append(parrafoseleccionado.find(':'))
#     delimitadores.append(parrafoseleccionado.find(';'))
#     #quitamos los -1 que son delimitadores no encontrados y nos puede dar lugar a errores
#     while -1 in delimitadores: 
#         delimitadores.remove(-1)
#     #y obtenemos el primero que aparece con el comando min (el menor es el primero)
#     finfrase = min(delimitadores)

#     #nuestra frase sera pues
#     frase = parrafoseleccionado[:finfrase]
#     print(frase)
#     #acordaros de cerrar el fichero si no lo habeis abierto con un with
#     fichero.close()    
#     return(frase)
# print(primerafrase(1))
#!/usr/bin/python
# -*- coding: utf-8 -*-

# www.pythondiario.com
# Cifrado Cesar

# LONG_LLAVE = 26


# def getOpcion():

#  while True:
#   print ('¿Tu quieres encriptar o desencriptar un mensaje?')
#   opcion = raw_input().lower()
#   if opcion in 'encriptar e desencriptar d'.split():
#    return opcion
#   else:
#    print ('Escribir "encriptar", "e" o "desencriptar", "d".')


# def getMensaje():
#  print ('Escribe el mensaje:')
#  return raw_input()

# def getLlave():
#  llave = 0
#  while True:
#   print('Ingresar la llave (1-%s)' % (LONG_LLAVE))
#   llave = int(input())
#   if (llave >= 1 and llave <= LONG_LLAVE):
#    return llave

# def getTraducirMensaje(opcion, mensaje, llave):
#  if opcion[0] == 'd':
#   llave = -llave
#  traducir = ''
 
#  for simbolo in mensaje:
#   if simbolo.isalpha():
#    num = ord(simbolo)
#    num += llave

#    if simbolo.isupper():
#     if num > ord('Z'):
#      num -= 26
#     elif num < ord('A'):
#      num += 26
#    elif simbolo.islower():
#     if num > ord('z'):
#      num -= 26
#     elif num < ord('a'):
#      num += 26

#    traducir += chr(num)
#   else:
#    traducir += simbolo
#  return traducir



# opcion = getOpcion()
# mensaje = getMensaje()
# llave = getLlave()

# print('El texto traducido es:')
# print(getTraducirMensaje(opcion, mensaje, llave))
import os.path
parrafoCifrar = int(input(f'Número de parrafo: '))
claveCifrado = int(input(f'Clave cifrado : '))
def primeraFrase(parrafo):
    #primero cargamos el fichero
    fichero = open(os.path.expanduser('~/Documents/apuntesPython/Curso/EDX/problemas/quijote.txt'))
    #lo leemos
    texto = fichero.read()
# # # #y seleccionamos el párrafo indicado en el parámetro 
    parrafos = texto.split('\n')
    #eliminamos los párrafos vacios tras el split 
    while '' in parrafos: 
        parrafos.remove('')      
        parrafoSeleccionado=parrafos[parrafo]
     #devolvemos el parrafo a encriptar
    return parrafoSeleccionado
encriptado = primeraFrase(parrafoCifrar)
print(encriptado)
def cifrar(texto, clave):
    longitud=len(texto); #Calculamos la longitud del texto para recorrerlo
    cifrar = ''
    for i in range (0, longitud+1):
        cifrar= cifrar + chr(i+clave)
    return cifrar
#print(cifrar(primeraFrase(parrafoCifrar),claveCifrado))
textoCifrado = cifrar(primeraFrase(parrafoCifrar), claveCifrado)
print(textoCifrado)
claveDescifrado =  int(input(f'Clave descifrado : '))
def desencriptar(texto,clave):
    longitud = len(texto)
    descifrar = ''
    for i in range(0,longitud+1):
        descifrar = descifrar + chr(i-clave)
    return descifrar
textoDescifrado = desencriptar(textoCifrado,claveDescifrado)
print(textoDescifrado)


            