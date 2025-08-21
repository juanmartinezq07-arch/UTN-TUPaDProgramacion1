#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Ejercicio 1")
print(f"Hola mundo!")
print("")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”

print("Ejercicio 2")
print("Escriba su nombre:")
nombre = input("")
print(f"Hola {nombre}!")
print("")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”

print("Ejercicio 3")
print("Ingrese su nombre")
nombre = input("")
print("Ingrese su apellido")
apellido = input("")
print("Ingrese su edad")
edad = int(input(""))
print("Ingrese su lugar de residencia")
residencia = input("")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
print("")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

print("Ejercicio 4")
print("Ingrese el radio de un círculo")
radio = int(input(""))

perimetro = 2 * 3.14 * radio 
area = 3.14 * (radio ** 2)

print(f"El perímetro es: {perimetro}")
print(f"El área es: {area}")
print("")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

print("Ejercicio 5")
print("Ingrese una cantidad de segundos")
segs = int(input(""))
hora = segs / 3600
print(f"{segs} segundos equivalen a {hora} hora.")
print("")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número

print("Ejercicio 6")
print("Ingrese un número para ver su tabla de multiplicar")
num = int(input(""))

print(f"0 X {num} = {num*0}")
print(f"1 X {num} = {num*1}")
print(f"2 X {num} = {num*2}")
print(f"3 X {num} = {num*3}")
print(f"4 X {num} = {num*4}")
print(f"5 X {num} = {num*5}")
print(f"6 X {num} = {num*6}")
print(f"7 X {num} = {num*7}")
print(f"8 X {num} = {num*8}")
print(f"9 X {num} = {num*9}")
print(f"10 X {num} = {num*10}")
print("")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Ejercicio 7")
print("Ingrese dos números enteros distintos a 0")
num1 = int(input(""))
num2 = int(input(""))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
print(f"La suma de {num1} + {num2} es: {suma}")
print(f"La resta de {num1} - {num2} es: {resta} ")
print(f"La multiplicación de {num1} x {num2} es: {mult}")
print(f"La división de {num1} / {num2} es: {div}")
print("")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.

print("Ejercicio 8")
print("Ingrese su altura y peso")
print("Altura:")
altura = float(input(""))
print("Peso:")
peso = int(input(""))

masa = peso / (altura)**2
print(f"Su índice de masa corporal es: {masa}")
print("")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit

print("Ejercicio 9")
print("Ingrese una temperatura en grados Celsius")
grado = int(input(""))

grados_fahrenheit = 9/5 * grado + 32
print(f"Temperatura en Celsius transformada a grados Fahrenheit: {grados_fahrenheit}")
print("")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

print("Ejercicio 10")
print("Ingrese 3 números.")
print("Número 1:")
num1 = int(input(""))
print("Número 2:")
num2 = int(input())
print("Número 3:")
num3 = int(input(""))

suma = num1 + num2 + num3
promedio = suma / 3

print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")