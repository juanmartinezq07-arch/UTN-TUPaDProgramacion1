#1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 
print("--- Ejercicio 1 ---")
print("")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario original: \n{precios_frutas}")
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(f"Diccionario nuevo: \n{precios_frutas}")
print("\n")

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 
print("--- Ejercicio 2 ---")
print("")
precios_frutas.update({"Banana": 1330, "Manzana" : 1700, "Melón": 2800})
print(f"Precios actualizados: \n{precios_frutas}")
print("\n")

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 
print("--- Ejercicio 3 ---")
print("")
lista_sin_precios = list(precios_frutas.keys())
print(f"Lista sin los precios: \n{lista_sin_precios}")
print("\n")

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
print("--- Ejercicio 4 ---")
print("")
contacto = {}
i = 0
for i in range(5):
    print("Ingrese el nombre de su contacto y su número de teléfono.")
    nombre_contacto = str(input("Nombre: "))
    numero_telefono = (input("Número: "))
    contacto[nombre_contacto] = numero_telefono
print("Decime el nombre de uno de tus contactos recientemente agregado")
consultar = input()
if consultar in contacto:
    print(f"El número de {consultar} es {contacto[consultar]}")
else:
    print("Contacto inexistente.")
print("\n")

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.
print("--- Ejercicio 5 ---")
print("")
print("Escribí una frase")
frase = str(input(""))
palabras = frase.lower().split()
palabras_unicas = set(palabras)
print(f"Palabras únicas: \n{palabras_unicas}")

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Contador de palabras repetidas: ")
print(contador_palabras)
print("\n")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.
print("--- Ejercicio 6 ---")
notas_alumno1 = []
notas_alumno2 = []
notas_alumno3 = []
nombres_alumnos = []
i = 0

print("Nombre del primer alumno:")
alumno = input()
nombres_alumnos.append(alumno)
print(f"Ingrese las notas de {alumno}")
for i in range(3):
    print(f"Nota {i+1}: ")
    nota = int(input())
    notas_alumno1.append(nota)

print("Nombre del segundo alumno:")
alumno = input()
nombres_alumnos.append(alumno)
print(f"Ingrese las notas de {alumno}")
for i in range(3):
    print(f"Nota {i+1}: ")
    nota = int(input())
    notas_alumno2.append(nota)

print("Nombre del tercer alumno:")
alumno = input()
nombres_alumnos.append(alumno)
print(f"Ingrese las notas de {alumno}")
for i in range(3):
    print(f"Nota {i+1}: ")
    nota = int(input())
    notas_alumno3.append(nota)

notas_alumno1 = tuple(notas_alumno1)
notas_alumno2 = tuple(notas_alumno2)
notas_alumno3 = tuple(notas_alumno3)

print("-----Promiedos------")
print(f"{nombres_alumnos[0]}: {sum(notas_alumno1)/3}")
print(f"{nombres_alumnos[1]}: {sum(notas_alumno2)/3}")
print(f"{nombres_alumnos[2]}: {sum(notas_alumno3)/3}")
print("\n")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
print("--- Ejercicio 7 ---")
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

aprobados_ambos = parcial1 & parcial2
print(f"Estudiantes que aprobaron ambos parciales: {aprobados_ambos}")

aprobados_solo_uno = parcial1 ^ parcial2
print(f"Estudiantes que aprobaron solo uno de los dos: {aprobados_solo_uno}")

aprobados_al_menos_uno = parcial1 | parcial2
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {aprobados_al_menos_uno}")
print("\n")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe.
print("--- Ejercicio 8 ---")
print("")
lista_productos_y_stock = {}
opcion = 0
while opcion != 4:
    print("Elige una de las siguientes opciones")
    print('''
        1 Consultar el stock de un producto ingresado. 
        2 Agregar unidades al stock si el producto ya existe. 
        3 Agregar un nuevo producto si no existe.
        4 Salir ''')
    opcion = int(input())
    match opcion:
        case 1:
            if not lista_productos_y_stock:
                print("No hay productos disponibles.")
                print("-"*40)
                continue
            consultar = input("Nombre del producto: ").capitalize()
            if consultar in lista_productos_y_stock:
                print(f"Stock disponible de {consultar}: {lista_productos_y_stock[consultar]}")
            else:
                print("Producto inexistente.")
            print("-"*40)
        case 2:
            if not lista_productos_y_stock:
                print("No hay productos disponibles.")
                print("-"*40)
                continue
            agregar_stock = input("Nombre del producto: ").capitalize()
            if agregar_stock in lista_productos_y_stock:
                stock_nuevo = int(input("Cantidad de stock que quieres agregar: "))
                lista_productos_y_stock[agregar_stock] += stock_nuevo
                print(f"Stock de {agregar_stock} actualizado a {lista_productos_y_stock[agregar_stock]}")
            else:
                print("Producto inexistente.")
            print("-"*40)
        case 3:
            print("Nombre del producto que queres agregar: ")
            agregar_producto = input("").capitalize()
            if agregar_producto in lista_productos_y_stock:
                print("Este producto ya está incorporado")
            else:
                lista_productos_y_stock[agregar_producto] = 0
                print("Producto agregado.")
            print("-"*40)
        case 4:
            print("Saliendo...")
print("\n")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora. 
print("--- Ejercicio 9 ---")
print("\n")
agenda = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Lunes", "14:30"): "Llamada con proveedor",
    ("Martes", "11:00"): "Clases de inglés",
    ("Miércoles", "08:00"): "Gimnasio",
    ("Miércoles", "17:00"): "Entrega de proyecto",
    ("Jueves", "10:30"): "Consulta médica",
    ("Viernes", "13:00"): "Almuerzo con cliente",
    ("Viernes", "18:00"): "Partido de fútbol",
    ("Sábado", "20:00"): "Cena con amigos",
    ("Domingo", "12:00"): "Visita familiar"
}
print("---- CONSULTAR AGENDA ----")
dia = input("Ingrese el día: ").capitalize()
hora = input("Ingrese la hora (xx:xx): ")
clave = (dia, hora)
if clave in agenda:
    print(f"La actividad del día {dia} a las {hora} es: {agenda[clave]}")
else:
    print("No hay actividades registradas en ese día y horario.")
    print("Actividades disponibles:")
    print(agenda)
print("\n")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores.
print("--- Ejercicio 10 ---")
print("")

diccionario_original = {"México" : "Ciudad de México", "Perú" : "Lima", "Paraguay" : "Asunción"}
print(f"Diccionario original: {diccionario_original}")

diccionario_invertido = {valor: clave for clave, valor in diccionario_original.items()}
print(f"Diccionario invertido: {diccionario_invertido}")