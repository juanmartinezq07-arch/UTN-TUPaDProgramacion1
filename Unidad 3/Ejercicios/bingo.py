import random
import time
from colorama import init, Fore , Style
init(autoreset=True)
print("Elige de que forma queres jugar:\n1.Normal\n2.Blackout")
opcion = int(input(""))
print("")
numeros = random.sample(range(1,51),25)
bingo = [numeros[i*5:(i+1)*5] for i in range(5)]
print("Cartón de bingo inicial:")
bolillas = list(range(1, 51))
random.shuffle(bolillas)
for fila in bingo:
    print(fila)
print("-"*20)
time.sleep(5)
terminado = True
i = 0
print("")
if opcion == 2:
    while terminado:
        encontrado = False
        bola = bolillas.pop(0)
        for f in range(5):
            for c in range(5):
                if bingo[f][c] == bola:
                    bingo[f][c] = 0
                    encontrado = True
        if encontrado:
            print(f"El número {Fore.YELLOW}{bola}{Style.RESET_ALL} ESTÁ en tu cartón!")
            print("")
            for fila in bingo:
                print(fila)
            print("-"*20)
        else:
            print(f"El número {Fore.YELLOW}{bola}{Style.RESET_ALL} NO está en tu cartón X")
            for fila in bingo:
                print(fila)
                print("-"*20)
        i = i + 1
        time.sleep(1.5)
        terminado = False
        for f in range(5):
            for c in range(5):
                if bingo[f][c] != 0:
                    terminado = True
if opcion == 1:
    fila_completa = False
    columna_completa = False
    while terminado:
        bola = bolillas.pop(0)
        encontrado = False
        for f in range(5):
            for c in range(5):
                if bingo[f][c] == bola:
                    bingo[f][c] = 0
                    encontrado = True
        if encontrado:
            print(f"El número {Fore.YELLOW}{bola}{Style.RESET_ALL} ESTá en tu cartón!")
            print("")
            for fila in bingo:
                print(fila)
            print("-"*20)
        else:
            print(f"El número {Fore.YELLOW}{bola}{Style.RESET_ALL} NO está en tu cartón X")
            for fila in bingo:
                print(fila)
            print("-"*20)
        time.sleep(2.4)
        i = i + 1
        for f in range(5):
            if all(num == 0 for num in bingo[f]):
                fila_completa = True
        for c in range(5):
            if all(bingo[f][c] == 0 for f in range(5)):
                columna_completa = True
        if fila_completa or columna_completa:
            terminado = False

print(Fore.GREEN + "👏FELICIDADES! BINGO COMPLETADO👏")