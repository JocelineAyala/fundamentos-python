'''
Clase:        Clase 9
Tema:         Manejo de lista
Ejercicio:    6.2.1  
Descripción:  Eliminando valores duplicados

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

lista = input().split()

sin_repetir = []

for i in lista:
    if i not in sin_repetir:
        sin_repetir.append(i)
    
resultado = " ".join(sin_repetir)

print(resultado)


