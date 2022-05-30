'''
Ejercicio 1
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
'''
letra = str(input("Introduce una letra: "))
if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o"  or letra.lower() == "u" :
    print("Tu letra es una vocal.")
else :
    print("Tu letra no es una vocal")

'''
Solución profesor
'''

letra = input("Ingresa una letra: ")

'''if letra.lower() == "a":
    print("Es una vocal")
else:
    if letra.lower() == "e":
        print("Es una vocal")
    else:
        if letra.lower() == "i":
            print("Es una vocal")
        else:
            if letra.lower() == "o":
                print("Es una vocal")
            else:
                if letra.lower() == "u":
                    print("Es una vocal")
                else:
                    print("NO es una vocal")'''

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("NO es una vocal")

'''
Ejercicio 2
Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
'''
entero = int(input("Introduce un número entero, si no es entero te capare los decimáles ;): "))
if entero > 0 :
    print("El valor absoluto de tu número es ", entero)
else :
    print("El valor absoluto de tu entero es ", entero * -1)

'''
Solución profesor
'''

numero = int(input("Ingresa el numero ENTERO: "))

if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: ".format(numero), abs(numero))