'''
Clase:        Clase 8
Tema:         Estructuras Iterativas
Ejercicio:    5.4.1 ¡Adivina el número!
Descripción:  Genera un número aleatorio enter 1 al 100 y pide al usuario adivinarlo.

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''


import random
numSecreto = random.randint(1,100)

while True:
    numUsuario = int(input("Ingrese un número entre 1 y 100: "))

    if numUsuario not in range(1,101):
        print("Este número no está dentro del rango solicitado")
        continue
    if numUsuario > numSecreto:
        print("El número secreto es menor")
        continue

    if numUsuario < numSecreto:
        print("El número secreto es mayor")
        continue

    if numUsuario == numSecreto:
        print("¡Felicidades! Has adivinado el número secreto: ", numSecreto)
        break


print("Fin del juego")