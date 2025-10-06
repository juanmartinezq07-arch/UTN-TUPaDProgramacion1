# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
print("---- Ejercicio 1 ----")
def imprimir_hola_mundo():
    print("Hola mundo!")
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
print("---- Ejercicio 2 ----")
def saluda_usuario(nombre):
    print(f"Hola {nombre}!")
usuario = input("Ingrese su nombre: ")
saluda_usuario(usuario)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
print("---- Ejercicio 3 ----")
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su appelido: "))
edad = int(input("Ahora ingrese su edad: "))
residencia = input("Por último, ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
print("---- Ejercicio 4 ----")
import math
def calcular_area_circulo(radio):
    area = math.pi * radio **2
    return round(area,2)
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    
    return round(perimetro,2)
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
print("---- Ejercicio 5 ----")
def segundos_a_horas(segundos):
    hora = segundos / 3600
    return round(hora,2)
segundos = int(input("Ingrese la cantidad de segundos para pasarlos a su hora correspondiente: "))
print(f"{segundos} segundos a hora son: {segundos_a_horas(segundos)}")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
print("---- Ejercicio 6 ----")
def tabla_multiplicar(numero):
    print(f''' 
        {numero} X 1 = {numero * 1}
        {numero} X 2 = {numero * 2}
        {numero} X 3 = {numero * 3}
        {numero} X 4 = {numero * 4}
        {numero} X 5 = {numero * 5}
        {numero} X 6 = {numero * 6}
        {numero} X 7 = {numero * 7}
        {numero} X 8 = {numero * 8}
        {numero} X 9 = {numero * 9}
        {numero} X 10 = {numero * 10}''')
num = int(input("Ingrese un número para mostrar su tabla de multiplicación del 1 al 10: "))
tabla_multiplicar(num)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
print("---- Ejercicio 7 ----")
def operaciones_basicas(a, b):
    operaciones = (f"{a} + {b} = {a + b}",
                    f"{a} - {b} = {a - b}",
                    f"{a} * {b} = {a * b}",
                    f"{a} / {b} = {a / b}")
    return operaciones
print("Ingrese dos números para realizar operaciones básicas.")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
resultados = operaciones_basicas(num1, num2)
for r in resultados:
    print(r)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
print("---- Ejercicio 8 ----")
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)
print("Ingrese su peso en kg:")
peso = float(input())
print("Ingrese su altura en metros:")
altura = float(input())
print(f"Su masa corporal (IMC) es de {calcular_imc(peso, altura)}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
print("---- Ejercicio 9 ----")
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return round(fahrenheit, 2)
print("Ingrese la temperatura en grados Celsius (ej: 25.1)")
temp_celsius = float(input())
print(f"{temp_celsius}°C grados celsius a Fahrenheit es {celsius_a_fahrenheit(temp_celsius)}°F")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
print("---- Ejercicio 10 ----")
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
print("Ingrese 3 números para saber su promedio.")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
print(f"El promedio de {num1}, {num2} y {num3} es {calcular_promedio(num1, num2, num3)}")