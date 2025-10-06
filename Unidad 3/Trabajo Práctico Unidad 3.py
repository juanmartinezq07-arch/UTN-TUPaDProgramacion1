print("---TP 3 Condicionales---")
print("")
#1)
edad = int(input("Ingrese su edad: "))
if edad >= 18 :
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
print("")
#2)
nota = int(input("Ingrese su nota: "))
if nota >= 6 :
    print("Aprobado")
else:
    print("Desaprobado")
print("")
#3)
num = int(input("Ingrese un número par: "))
if num % 2 == 0 :
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print("")
#4)
edad = int(input("Ingresu edad"))
if edad < 12 :
    print("Niño/a")
if edad >= 12 and edad < 18 :
    print("Adolescente")
if edad >= 18 and edad < 30 :
    print("Adulto/a joven")
if edad >= 30 :
    print("Adulto/a")
print("")
#5)
clave = input("Ingrese una contraseña entre 8 y 14 caracteres")
validar_clave = len(clave)
if validar_clave >= 8 and validar_clave <= 14 :
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("")
#6)
from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Moda: {moda}\nMediana: {mediana}\nMedia: {media}")
if media > mediana and mediana > moda:
    print("Sesgo positivo")
if media < mediana and mediana < moda:
    print("Sesgo negativo")
if media == mediana and mediana == moda:
    print("Sin sesgo")
#7)
frase = str(input("Ingrese una frase o palabra: "))
if frase[-1].lower() in "aeiou":
    frase = frase + "!"
print("")
#8)
nombre = str(input("Ingrese su nombre: "))
print("Ingrese un número según lo que quiera hacer:")
print("1. Si quiere su nombre en mayúsculas.\n2. Si quiere su nombre en minúsculas.\n3. Si quiere su nombre con la primera letra mayúscula")
opcion = int(input())
if opcion == 1 :
    nombre = nombre.upper()
    print(nombre)
elif opcion == 2 :
    nombre = nombre.lower()
    print(nombre)
elif opcion == 3:
    nombre = nombre.title()
    print(nombre)
else:
    print("No eligió ninguna opción ofrecida")
print("")
#9)
magnitud = float(input("Ingrese la magnitud de un terremoto"))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4 :
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6 :
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >=6 and magnitud < 7 :
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7 :
    print("Extremo (puede causar graves daños a gran escala).")
#10
hemisferio = str(input("En que hemisferio se encuentra N/S: "))
hemisferio = hemisferio.lower()
mes = int(input("Ingrese el mes del año que se encuentra: "))
dia = int(input("Ingrese que día es: "))
if mes == 2 and (dia < 1 or dia > 28):
    print("Febrero solo tiene 28 días.")
elif dia > 31 or dia < 1:
    print("Día incorrecto.")
elif mes > 12 or mes < 1:
    print("Mes incorrecto.")
else:
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia < 21):
        estacion_n = "Invierno"
        estacion_s = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia < 21):
        estacion_n = "Primavera"
        estacion_s = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia < 21):
        estacion_n = "Verano"
        estacion_s = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia < 21):
        estacion_n = "Otoño"
        estacion_s = "Primavera"

    if hemisferio == "n":
        print(f"Estás en {estacion_n}.")
    elif hemisferio == "s":
        print(f"Estás en {estacion_s}.")
    else:
        print("Hemisferio incorrecto.")