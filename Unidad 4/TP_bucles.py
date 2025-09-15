import time
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando nun número por línea
print("Ejercicio 1")
i = 0
for i in range(101):
    time.sleep(0.5)
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
print("Ejercicio 2")
print("Ingrese un número: ")
numero = int(input())
aux = numero
contador = 0
while numero > 0:
    numero = numero // 10  
    contador = contador  + 1 
print(f"La cantidad de dígitos de: {contador}")
print("")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
print("Ejercicio 3")
print("Ingrese dos números: ")
num1 = int(input())
num2 = int(input())
suma = 0
if num1 > num2:
    for i in range(num2 + 1,num1):
        suma = suma + i
elif num2 > num1:
    for i in range(num1 + 1,num2):
        suma = suma + i
print(f"La suma de los números entre {num1} y {num2} es: {suma}")
print("")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
print("Ejercicio 4")
num = 1
total = 0
print("Ingresa cualquier número para ir sumandolo, si deseas detener el programa ingrese 0.")
while num != 0:
    num = int(input())
    total = total + num
print(f"La suma total de los números es de: {total}")
print("")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("Ejercicio 5")
import random
num_aleatorio = random.randint(0,9)
num = 10
print("Adivina el número entre 0 y 9:")
while num != num_aleatorio:
    num = int(input())
print("Lo conseguiste!")
print("")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
print("Ejericcio 6")
for i in range(100,0, -2):
    time.sleep(0.5)
    print(i)
print("")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
print("Ejercicio 7")
suma = 0
num = int(input("Ingrese un número: "))
for i in range(num):
    suma = suma + i
print(f"La suma de todos los números comprendidos entre 0 y {num} es: {suma}")
print("")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("Ejercicio 8")
cantidad = int(input("Ingrese la cantidad de números que quieras ingresar: "))
par = 0
impar = 0
positivo = 0
negativo = 0
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    if num > 0:
        positivo = positivo + 1
    elif num < 0:
        negativo = negativo + 1
print(f'''Números pares: {par}
    Números impares: {impar}
    Números positivos: {positivo}
    Números negativos: {negativo}''')
print("")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
print("Ejercicio 9")
cantidad = int(input("Ingrese la cantidad de números que quieras ingresar: "))
suma = 0
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma = suma + num
promedio = suma / cantidad
print(f"La media de los números es de: {promedio}")
print("")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("Ejercicio 10")
numero = int(input("Ingrese un número: "))
invertido = 0
while numero > 0:
    digito = numero % 10 
    invertido = invertido * 10 + digito
    numero = numero // 10 
print(f"El número invertido es: {invertido}")

