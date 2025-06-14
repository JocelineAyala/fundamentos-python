'''
Clase:        Clase 11
Tema:         10. Manejo de matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  Dada una matriz cuadrada comprobar si la matriz es simétrica con respecto a su diagonal principal.

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

N = int(input())
lista = []
for i in range(N):
    raw_input = input()
    temp_list = list(map(int, raw_input.split(",")))
    lista.append(temp_list)

simetrica = True

for i in range(N):
    for j in range(N):
        if lista [i][j] != lista[j][i]:
            simetrica = False

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
            
