#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range.
print("Ejercicio 1")
lista_multiplos = []
i = 0
for i in range(1,101):
    if i % 4 == 0:
        lista_multiplos.append(i)
print(f"Lista con los múltiplos de 4: {lista_multiplos}")

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo.
print("Ejercicio 2")
lista = ["Argentina", 18, True, "River", "Mundial"]
print(lista[3])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
#pantalla.
print("Ejercicio 3")
lista_vacia = []
print(f"Lista vacía: {lista_vacia}")
lista_vacia.append("Maravilla")
lista_vacia.append("Jazmin")
lista_vacia.append("Coca-Cola")
print(f"Lista con elementos agregados: {lista_vacia}")

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla.
print("Ejercicio 4")
animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista sin cambiar: {animales}")
animales[1] = "loro"
animales[-1] = "oso"
print(f"Lista cambiada: {animales}")

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print("Ejercicio 5")
#crea una lista con 5 elementos que son enteros
numeros = [8, 15, 3, 22, 7]
#Acá busca quitar el número más alto (con remove lo saca,y con max encuentra el valor más alto)
numeros.remove(max(numeros))
#imprime la lista cambiada
print(numeros)

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros. 
print("Ejercicio 6")
i = 0
lista = []
for i in range(10,31,5):
    lista.append(i)
print(lista[0])
print(lista[1])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 
print("Ejercicio 7")
autos = ["sedan", "polo", "suran", "gol"]
print(f"Lista sin modificar: {autos}")
autos[1] = 203
autos[2] = 209
print(f"Lista modificada: {autos}")

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla.
print("Ejercicio 8") 
dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla
print("Ejercicio 9")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(f"Lista sin modificar: {compras}")
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(f"Lista modificada: {compras}")

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla.
print("Ejercicio 10")
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)