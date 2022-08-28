'''
Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas 
el nombre del usuario tantas veces como el número introducido.
'''
# nombre = input(f'Nombre: ')
# veces = int(input(f'Veces a imprimir: '))
# for i in range(0,veces):
#     print(i+1, ' ', nombre)

# nombre = input("¿Cómo te llamas? ")
# n = input("Introduce un número entero: ")
# print((nombre + "\n") * int(n))

'''
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
# nombre = input(f'Escribe tu nombre completo: ')
# print(f'{nombre.lower()}')
# print(f'{nombre.upper()}')
# print(f'{nombre.title()}')

'''
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''
# nombre = input(f'Nombre: ')
# print(f'{nombre.upper()} tiene {len(nombre)} letras.')

'''
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''
# telf = input(f'Numero de teléfono: ')
# print(f'El número simple es: {telf[4:-3]}')
'''
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola 
y muestre por pantalla la frase invertida.
'''
# frase = input(f'Frase: ')
# esarf = ''.join(reversed(frase))
# print(f'{frase}<->{esarf}')

'''
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''
# frase = input(f'Frase: ')
# vocal = input(f'Vocal: ')
# mayuscula = ''
# for i in frase:
#     if i == vocal:
#         print(i)
#         mayuscula = i.upper()
#         frase2 = frase.replace(i,mayuscula)
# print(frase2)

# frase = input("Introduce una frase: ")
# vocal = input("Introduce una vocal en minúscula:  ")
# print(frase.replace(vocal, vocal.upper()))

'''
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola 
y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.
'''
# correo = input(f'Correo: ')
# correo2 = correo[0:correo.find('@')+1] + 'ceu.es'
# print(f'El correo nuevo es: {correo2}')

'''
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''
# precio = float(input(f'Introduce el precio:  '))
# precio2 = int(round(precio, 2))
# precio3 = str(precio)
# punto = precio3.index('.')
# extraer = precio3[punto+1:punto+3]
# print(f'Precio: {precio2}.{extraer}')
# print(f'euros: {abs(precio2)}')
# print(f'Decimales: {extraer}')

# precio = input("Introduce el precio del producto con dos decimales:  ")
# print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

'''
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''
fecha = input(f'Fecha de nacimiento dd/mm/aaaa: ')
dia = fecha[:fecha.find('/')]
mes = fecha[fecha.find('/')+1:]
anyo = fecha[fecha.find('/'):]
print(f'Hoy es {dia} del {mes} del año {anyo}')