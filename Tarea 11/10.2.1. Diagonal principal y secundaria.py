'''
Clase:        Clase 11
Tema:         10. Manejo de matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada, imprime los elementos de la diagonal principal y secundaria.

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

diagonalPrincipal = []
diagonalSecundaria = []

for i in range(N):
    for j in range(N):
        if i == j:
            diagonalPrincipal.append(lista[i][j])

for i in range(N):
    for j in range(N):
        if i + j == N - 1:
            diagonalSecundaria.append(lista[i][j])

print(diagonalPrincipal)
print(diagonalSecundaria)
