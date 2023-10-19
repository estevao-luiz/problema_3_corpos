# -*- coding: utf-8 -*-

"""Este código recebe um arquivo constando o comportamento inicial
do movimento de três corpos e devolve outro arquivo com o movimento
desses três corpos durante um dado tempo"""

import math

grav = 6.67 * (10**(-11)) # constante gravitacional

'''
Vamos convencionar que um corpo é uma lista de 5
elementos
	[rx, ry, vx, vy, m]
rx - posição em x
ry - posição em y
vx - velocidade em x
vy - velocidade em y
m - massa

Além disso, o arquivo inicial é do tipo:
"
corpo1
corpo 2
corpo 3
tempo total
intervalo de tempo para leitura do movimento
"
'''

def dist(body_a, body_b):
    
    """ (list, list) -> (float)

	Esta função recebe dois corpos body_a, body_b.
	Retorna a distância entre eles. """
    
    dist = 0

    dist = math.sqrt(((body_a[0]-body_b[0])**2)+((body_a[1]-body_b[1])**2))
    # Fórmula da distância entre dois ponto, de acordo com a Gemetria analítica
    # D = ((x1 - x2)^2 + (y1-y2)^2)^1/2
    
    return dist


def forca(index, bodies):
   
    """ (int, list) -> (float)

	Esta função recebe um inteiro id, uma lista de
	corpos bodies. Retorna  a força resultante no 
	corpo bodies[id]. """
    
    fx, fy = 0, 0
    i = 0
    
    
    for i in range(0, 3):
        if i != index:
            fo = ((grav*bodies[index][4]*bodies[i][4])/((dist(bodies[index], bodies[i]))**2)) # resultante gravitacional
            fx, fy = fx + (fo/dist(bodies[index], bodies[i]))*((bodies[i][0])-(bodies[index][0])), fy + (fo/dist(bodies[index], bodies[i]))*((bodies[i][1])-(bodies[index][1]))
            # Cada componente equivale a f_atual = f_antiga + dr*|F|/dist tomada de dois a dois corpos.
            # Em que:
            # dr = r_final - r_inicial;
            # |F| = fo = módulo da resultante gravitacional;
            # dist = distância entre os dois corpos estudados.
            
    return fx, fy        

	
def atualiza(body, fx, fy, dt):
	
    """(list, float, float, float) -> (list)

	Esta função recebe um corpo, as forças fx, fy
	atuando no mesmo e um intervalo	de tempo dt
	e retorna o corpo atualizado após o intervalo. """

    new_body = []


    a = [fx/body[4], fy/body[4]] #a=F/m
    v = [body[2]+(a[0]*dt), body[3]+(a[1]*dt)] #v = vo + a*t 
    r = [body[0]+(v[0]*dt), body[1]+(v[1]*dt)]  #r = ro * v*t
  
    new_body = [r[0], r[1], v[0], v[1], body[4]]
    
    new_body = [float(x) for x in new_body]

    return new_body

def main():


    file_name = "3body.in"
    FILE_IN = open(file_name)
    FILE_OUT = open((file_name.split('.'))[0] + ".out", "w", encoding = 'utf-8')

    bodies = [[] for k in range(3)] # Declara 3 vetores de 5 elementos, 1 para cada corpo
    F = [[0, 0], [0, 0], [0, 0]] #Força em dois componentes de cada corpo.
    
    for i in range(0, 3): # le os corpos
        bodies[i] = [float(x) for x in FILE_IN.readline().split()]
        #print(bodies[i])

    t = int(FILE_IN.readline()) # tempo máximo
    dt = int(FILE_IN.readline()) # intervalo de tempo		
    FILE_IN.close()

    # Escreve a posição inicial de cada corpo.
    for i in range(0, 3):
        FILE_OUT.write("{:.10e} {:.10e} ".format(bodies[i][0], bodies[i][1]))
    FILE_OUT.write('\n')
    
    # Escreve a posição de cada corpo em file_name.out
    # Fazendo a contagem de dt em dt, para cada corpo calcula-se as componetes Fx e Fy,
    # logo depois atualiza-se as condições de movimento do corpo.
    for i in range(0, t, dt): 
        for j in range(0, 3): #calcula as componentes das forças nos respectivos corpos
            F[j][0], F[j][1] = forca(j, bodies) 
        for k in range(0, 3): #atualiza as condições de movimento, corpo a corpo de acordo com F.
            bodies[k]= atualiza(bodies[k], F[k][0], F[k][1], dt)
            FILE_OUT.write("{:.10e} {:.10e} ".format(bodies[k][0],bodies[k][1]))
        FILE_OUT.write('\n')

    
    FILE_OUT.close()

main()
