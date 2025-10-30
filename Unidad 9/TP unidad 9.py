# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
print("Ejercicio 1")
print("\n")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_numeros_y_factorial():

    try:
        num = int(input("Ingrese un número entero positivo para calcular factoriales hasta ese límite: "))
        
        if num < 0:
            print("Por favor, ingrese un número entero positivo.")
            return

        print(f"\nEl factorial de {num} es: {factorial(num)}")
        
        print(f"\nLos factoriales de los números enteros entre 1 y {num}:")

        for i in range(1, num + 1): 
            resultado = factorial(i)
            print(f"El factorial de {i} es: {resultado}")

    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")

mostrar_numeros_y_factorial()
print("\n")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique
print("Ejercicio 2")
print("\n")

def fibonacci(n): 
    if n == 0 or n == 1: 
        return n 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2) 

def mostrar_fibo():
    try:
        num = int(input("Ingrese un número para calcular el valor de la serie Fibonacci en esa posición: "))
        
        print(f"\nEl valor de la serie de Fibonacci de {num} es: {fibonacci(num)}")

        print(f"\nLa serie completa hasta {num}:")
        for i in range(0, num + 1):
            resultado = fibonacci(i)
            print(resultado)
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")  

mostrar_fibo()
print("\n")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general.
print("Ejercicio 3")
print("\n")

def potenciar_numero(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potenciar_numero(base, exponente - 1)

def probar_potencia():
    print("--- Cálculo de Potencia Recursiva ---")
    try:
        n = int(input("Ingrese el número base (n): "))
        exp = int(input("Ingrese el exponente (m): "))
        
        resultado = potenciar_numero(n, exp)
        
        print(f"\nResultado usando recursividad:")
        print(f"{n}^{exp} = {resultado}")
        

        print(f"Resultado de verificación: {n**exp}")

    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")

probar_potencia()
print("\n")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
print("Ejercicio 4")
print("\n")

def decimal_a_binario(num):
    if num == 0:
        return ""
    cociente = num // 2
    resto = num % 2

    return decimal_a_binario(cociente) + str(resto)

def llamar_conversion():
    try:
        num = int(input("Ingrese un número entero positivo en base decimal: "))
        if num == 0:
            resultado_binario = "0"
        else:
            resultado_binario = decimal_a_binario(num)

        print(f"\nEl número {num} en binario es: {resultado_binario}")
        
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")

llamar_conversion()
print("\n")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
print("Ejercicio 5")
print("\n")

def es_palindromo(palabra):
    if palabra[0] != palabra [-1]:
        return False
    elif len(palabra) <= 1:
        return True
    else:
        return es_palindromo(palabra[1:-1])

palabra = str(input("Ingrese un texto para saber si es palindromo: "))
if es_palindromo(palabra):
    print(f"La palabra {palabra} es palindromo.")
else:
    print(f"La palabra {palabra} no es palindromo.")
print("\n")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
print("Ejercicio 6")
print("\n")

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
try:
    num = int(input("Ingrese un número positivo, y te devolveré la suma de todos sus dítgitos: "))
    print(f"La suma de todos los digitos de {num} es: {suma_digitos(num)}")
except ValueError:
    print("Entrada no válida. Ingrese un número entero.")
print("\n")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo
print("Ejercicio 7")
print("\n")

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)

try:
    niveles_maximos = int(input("Ingrese la altura máxima de bloques q tendrá la pirámide: "))
    
    if niveles_maximos < 1:
        print("La altura debe ser al menos 1.")
    else:
        print("\n--- Resultados de la Pirámide ---")
        
        for i in range(1, niveles_maximos + 1):
            total = contar_bloques(i)
            print(f"Nivel {i}: El total de bloques es {total}")
            
        print("--------------------------------")
except ValueError:
    print("Entrada no válida. Ingrese un número entero.")
print("\n")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
print("Ejercicio 8")
print("\n")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        contador = 1 if ultimo_digito == digito else 0

        return contador + contar_digito(numero // 10, digito)

try:
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito entre 0 y 9: "))
    if numero >= 0 and digito in range(0,10):
        print(f"El dígito {digito} aparece {contar_digito(numero,digito)} vez/veces en el número {numero}.")
    else:
        print("ERROR: No ingrasaste un número postivio o un dígito entre 0 y 9.")
except ValueError:
    print("Entrada no válida. Ingrese un número entero")