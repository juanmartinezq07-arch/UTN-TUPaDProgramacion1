#bucle for
from colorama import Fore, Style, init
init(autoreset=True)
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Ingrese cuanto deseas mover: "))
texto = input("Ingrese el mensaje a cifrar: ").lower()
resultado = ""

for letra in texto:
    if letra in alfabeto:   
        indice = alfabeto.index(letra)
        nueva_letra = alfabeto[(indice + corrimiento) % len(alfabeto)]
    else:
        nueva_letra = letra
    resultado = resultado + nueva_letra
print(f"Mensaje sin cifrar: {Fore.YELLOW}{texto}")
print(f"Mensaje cifrado: {Fore.RED}{resultado}")

#bucle while
import random
print("---------------------Piedra, Papel o Tijeras---------------------")
limite = int(input("Elige el límite de rondas para jugar: "))
salir = False
puntaje_IA = 0
puntaje_JG = 0
rondas = 0
while salir == False:
    decicion_Ia = random.randint (1,3)
    decicion = int(input("Elige una opcion:\n 1.Piedra \n 2.Papel \n 3.Tijeras\n 4.Salir\n "))
    print("la decicion de la Ia fue: ", decicion_Ia)
    if decicion != decicion_Ia :
        if decicion == 1 and decicion_Ia ==2:
            print ("Perdiste")
            puntaje_IA = puntaje_IA + 1
            rondas = rondas + 1
        elif decicion == 1 and decicion_Ia == 3:
            print ("Ganaste")
            puntaje_JG = puntaje_JG + 1
            rondas = rondas + 1
        if decicion == 2 and decicion_Ia == 3:
            print ("Perdiste")
            puntaje_IA = puntaje_IA + 1
            rondas = rondas + 1
        elif decicion == 2 and decicion_Ia == 1:
            print ("Ganaste")
            puntaje_JG = puntaje_JG + 1
            rondas = rondas + 1
        if decicion == 3 and decicion_Ia == 1:
            print ("Perdiste")
            puntaje_IA = puntaje_IA + 1
            rondas = rondas + 1
        elif decicion == 3 and decicion_Ia == 2:
            print ("Ganaste")        
            puntaje_JG = puntaje_JG + 1
            rondas = rondas + 1
    else: 
        print ("Empate")
    if decicion == 4:    
        salir = True
    if limite == rondas :
        salir = True
print(Fore.CYAN + "/// MARCADOR ///")
print(Fore.WHITE + f"Puntaje de la IA: {Fore.GREEN}{puntaje_IA}")
print(Fore.WHITE + f"Puntaje del Jugador: {Fore.GREEN}{puntaje_JG}")
if puntaje_JG > puntaje_IA :
    print(Fore.GREEN + "FELICIDADES, HAS GANADO!!!")
elif puntaje_IA > puntaje_JG :
    print(Fore.RED + "HAS SIDO DERROTADO! SUERTE LA PRÓXIMA")
else:
    print(Fore.YELLOW + "WOW, HAN EMPATADO!")