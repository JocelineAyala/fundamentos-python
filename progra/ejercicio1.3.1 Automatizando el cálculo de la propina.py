'''
Clase:        Clase 1
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3 Ejercicios prácticos de exploración
Descripción:  Automatizando el cálculo de la propina

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

cuenta=float(input("Escribe el total de la cuenta: "))
porcentajePropina=float(input("Escribe el porcentaje de propina: "))
total = ((cuenta*porcentajePropina)/100) + cuenta

print(f"La cuenta es de {cuenta} y el porcentaje de propina de {porcentajePropina} su total es de: {total}")