'''
Clase:        Clase 11
Tema:         10. Manejo de matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  Dada una matriz binaria, verificar cuántos elementos con valor de 1 hay en las celdas vecinas.

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

N = int(input())
M = int(input())

matriz = []
for i in range(N):
    raw_input = input()
    temp_list = list(map(int, raw_input.split(",")))
    matriz.append(temp_list)


def buscarVecinos (matriz, i, j):
    if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]):
        return 1 if matriz[i][j] == 1 else 0
    return 0

resultado = []

for i in range(N):
    fila = []
    for j in range(M):
        total = (
            buscarVecinos(matriz, i - 1, j) +
            buscarVecinos(matriz, i + 1, j) +
            buscarVecinos(matriz, i, j - 1) +
            buscarVecinos(matriz, i, j + 1) +
            buscarVecinos(matriz, i - 1, j - 1) +
            buscarVecinos(matriz, i - 1, j + 1) +
            buscarVecinos(matriz, i + 1, j - 1) +
            buscarVecinos(matriz, i + 1, j + 1)
        )
        fila.append(total)
    resultado.append(fila)
    
for fila in resultado:
    print(" ".join(map(str, fila)))