#Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el monto de la cuenta.
#El programa debe:
#Pedir al usuario el monto total de la cuenta.
#Calcular la propina sugerida al 10%.
#Calcular la propina sugerida al 15%.
#Calcular el total a pagar en ambos casos (cuenta + propina).
#Mostrar todos los resultados en pantalla.

print("Calcular propina:")
print("")
print("Ingrese el monto total de la cuenta:")
monto = int(input(""))

propina1 = 0.10
propina_sugerida = monto * propina1
print(f"Propina sugerida con 10%: {propina_sugerida}")

monto_total = monto + propina_sugerida
print(f"El monto total con la propina sugerida del 10% es de: ${monto_total}")
print("")

propina2 = 0.15
propina_sugerida = monto * propina2
print(f"Propina sugerida con 15%: {propina_sugerida}")

monto_total = monto + propina_sugerida
print(f"El monto total con la propina sugerida del 15% es de: ${monto_total}")