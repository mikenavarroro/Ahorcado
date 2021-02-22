import random

abecedario = list('abcdefghijklmnñopqrstuvwxyz')
num_letras = random.randint(2, 23)
palabra_uno, palabra_dos = "",""

for _ in range(num_letras):
    palabra_uno += random.choice(abecedario)
    palabra_dos += random.choice(abecedario)

palabras = [palabra_uno, palabra_dos]
