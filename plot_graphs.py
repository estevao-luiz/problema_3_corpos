# -*- coding: utf-8 -*-

import matplotlib
from matplotlib import pyplot as plt

name_file = str(input("Nome do arquivo com os dados: "))

data = [[] for _ in range(6)]

# leitura dos dados
size = 0
with open(name_file) as file:
	for lines in file:
		line = list(map(float, (lines.strip()).split(' ')))
		size_line = len(line)

		if size == 0:
			size = size_line

		if size != size_line or size_line & 1: #verifica se size_line é ímpar (dados faltosos).
			print("Arquivo " + name_file + " é inválido")
			exit(1)

		for j in range(0, len(line)):
			data[j].append(line[j])

# cores dos corpos
color = ["Blue", "Red", "Green"]

# desenha os corpos

for i in range(0, size_line//2):
	plt.scatter(data[2 * i], data[2 * i + 1], s = .1, color = color[i], label = "Corpo " + str(i + 1)) # desenha o corpo 1

#plt.xlim([-1 * (10**11), 1 * (10**11)]) # define as dimensões do eixo x
#plt.ylim([-1.25 * (10**11), 1.25 * (10**11)]) # define as dimensões do eixo y
#matplotlib.pyplot.gcf().set_size_inches(10.5, 12.5) # define o tamanho das imagens

plt.title("Movimento dos Três Corpos em 2D") # adiciona título ao gráfico.
#plt.axis('off')  # omite os eixos
plt.savefig(name_file+".png") # salva a figura com o formato preferido.
