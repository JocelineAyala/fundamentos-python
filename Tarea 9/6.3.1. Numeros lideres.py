'''
Clase:        Clase 8
Tema:         Estructuras Iterativas
Ejercicio:    6.3.1. Números líderes
Descripción:  Pide una lista de números al usuario, imprime todos los números líderes (números mayores al de su derecha)

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-06-01
Estado:       [ Terminado ]
'''

lista = input().split()

conversionNum = []
for n in lista:
    conversionNum.append(int(n))

numLider = []

i = 0

while i < len(conversionNum) - 1:
    actual = conversionNum[i]
    siguiente = conversionNum[i + 1]

    if actual > siguiente:
        numLider.append(actual)

    i += 1

for num in numLider:
    print(num, end=" ")