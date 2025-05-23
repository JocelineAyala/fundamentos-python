'''
Clase:        Clase 1
Tema:         Bloque condicional
Ejercicio:    2.4 ¡Avanza al siguiente nivel!
Descripción:  El número mágico

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

num=int(input("Escribe el número para determinar si es mágico o normal: "))

if num in range (1, 1000000000000000001):
    if num % 7 == 0:
        print("Mágico")
    elif num % 5 == 0:
        print("Normal")
else:
    print("Número fuera de rango")