from palabras import palabras
import random

palabra = random.choice(palabras)
vidas = 7
letras_anteriores = []

for i in range(len(palabra)):
    print("-", end= " ")
print()

while vidas != 0:
    respuesta = input()
    if respuesta in palabra:
        letras_anteriores.append(respuesta)
        aux = 0
        for i in palabra:
            if i in letras_anteriores:
                print(i, end= " ")
                aux += 1
            else:
                print("-", end= " ")
        if aux == len(palabra):
            break
        print()
    else:
        vidas -= 1
        print("La letra", respuesta, "no está en la palabra")
        if vidas > 1:
            print("Te quedan", vidas, "vidas")
        elif vidas == 1:
            print("Te queda 1 vida")
        for i in palabra:
            if i in letras_anteriores:
                print(i, end= " ")
                aux += 1
            else:
                print("-", end= " ")
        print()

if vidas == 0:
    print("\nPerdiste\nLa palabra era", palabra)
else:
    print("\nGanaste\nLa palabra era", palabra)
