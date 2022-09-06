'''
Cargar el fichero "Quijote.txt" del ejercicio del tema 7 con el código de caracteres correcto, crear una función que permita seleccionar el número de párrafo que se solicita más abajo (empezando a contar por 0 para el primer párrafo) como en el ejercicio del tema 7 y le aplique a ese párrafo una encriptación por desplazamiento de código (como la explicada en el tema 6) con el desplazamiento positivo indicado más abajo, devolviendo el párrafo encriptado y obteniendo a la vez el valor numérico del código del caracter que se encuentra en la posición del párrafo que se indica más abajo (empezando a contar por 0 para el primer caracter del párrafo). Guardar el párrafo encriptado en una variable y crear una función a la que pasarle el párrafo encriptado y el desplazamiento aplicado y que permita desencriptar el texto aplicando el mismo desplazamiento de código en sentido inverso (esta parte no se evalua).
Número de párrafo: 1
Desplazamiento del código de encriptación: 8
Número de carácter dentro del párrafo: 321
'''
parrafoCifrar = int(input(f'Número de parrafo: '))
claveCifrado = int(input(f'Clave cifrado : '))
def primeraFrase(parrafo):
    #primero cargamos el fichero
    fichero = open('c:/Users/Admin.Lazaro/probaqndo/python/apuntesPython/Curso/EDX/problemas/quijote.txt', encoding="utf-8")
    #lo leemos
    texto = fichero.read()
    #y seleccionamos el párrafo indicado en el parámetro 
    parrafos = texto.split('\n')
    #eliminamos los párrafos vacios tras el split 
    while '' in parrafos: 
        parrafos.remove('')      
        parrafoSeleccionado=parrafos[parrafo]
     #devolvemos el parrafo a encriptar
    return parrafoSeleccionado
parrafoEncriptar = primeraFrase(parrafoCifrar)
print(parrafoEncriptar)
def cifrar(clave):
    cifrado = ''
    for i in parrafoEncriptar:
        cifrado= cifrado + chr(ord(i)+clave)
    return cifrado
print(cifrar(claveCifrado))
claveDescifrado =  int(input(f'Clave descifrado : '))
def desencriptar(clave):
    cifrado =cifrar(claveCifrado)
    descifrar = ''
    for i in cifrado:
        descifrar = descifrar + chr(ord(i)-clave)
    return descifrar
textoDescifrado = desencriptar(claveDescifrado)
print(textoDescifrado)
textoCifrado = cifrar(claveCifrado)
dato = int(input(f'Número de orden del caracter a identificar: '))
caracter = textoCifrado[dato]
orden = ord(caracter)
print(orden, caracter) 
print(ord('M'))

            