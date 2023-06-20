# Ejercicio 1

# Escribir una tupla con los meses del año, luego, pide al usuario un numero, 
# el que haya ingresado, es el mes que debe mostrar en la tupla

meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre', 'Octubre','Noviembre','Diciembre')
mes = int(input('Ingresa en número de mes a mostrar: '))
print('El mes número ', mes, ' es ', meses[mes-1])






#Ejercicio 2

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
anyos = input("¿Cuántos años tienes?\n")
valor = int(anyos)
for i in range(1,valor+1):
    print(i,"\n")