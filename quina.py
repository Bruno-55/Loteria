"""
	Esse programa vai tentar adivinhar os numeros da quina.
"""
import os

from random import randint


jogo = []

# Esta funcao vai continuar apresentando numeros aleatorios ate 15 dezenas nao repetidas popularem a lista "jogo"
while len(jogo) < 5:
	dezena = randint(1, 80)
	if dezena in jogo:
		pass
	else:
		jogo.append(dezena)

jogo.sort()

print(jogo)

os.system("pause")