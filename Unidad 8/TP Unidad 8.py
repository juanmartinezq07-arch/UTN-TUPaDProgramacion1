import os

#crear archivo con 3 productos
with open("productos.txt", "w",  encoding="utf-8") as archivo:
    archivo.write('nombre,precio,cantidad\n')
    archivo.write('Lapiz,520,10\n')
    archivo.write('Perfume,21000,6\n')
    archivo.write('Camiseta de Argentina,55200,14\n')

#leer y mostrar los productos
with open("productos.txt", "r") as archivo:
    next(archivo)

    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Productos: {nombre} | Precios: {precio} | Cantidad: {cantidad}")
        print("\n")

#agregar productos
with open("productos.txt", "a") as archivo:
    try:
        agregar_producto = str(input("Nombre del producto que quiere agregar: "))
        agregar_precio = int(input("Precio del producto: "))
        agregar_cantidad = int(input("Cantidad del producto: "))
        print("\n")
        archivo.write(f'{agregar_producto},{agregar_precio},{agregar_cantidad}')
    except ValueError:
        print("ERROR. Valor incorrecto.")
        print("\n")

#cargar productos en diccionario
productos = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    next(archivo)  # saltar encabezado

    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

# buscar productos por nombre y mostrar sus datos
encontrado = False

with open("productos.txt", "r", encoding="utf-8") as archivo:
    next(archivo)

    buscar = input("Nombre de producto que quiere buscar: ")
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        if buscar.lower() == nombre.lower():
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
            encontrado = True
            print("\n")
            break

if not encontrado:
    print(f"El producto '{buscar}' no existe.")
    print("\n")

#guardar productos
with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    print("Productos actualizados: ")
    print("")
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print(productos)