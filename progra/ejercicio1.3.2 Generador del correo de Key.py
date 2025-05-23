'''
Clase:        Clase 1
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3 Ejercicios prácticos de exploración
Descripción:  Generador del correo de Key

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

nombreCompleto=input("Escribe tu nombre completo: ")

dividido =nombreCompleto.split()

primerNombre, segundoNombre, primerApellido, segundoApellido = dividido

print (f"{primerNombre}.{primerApellido}@keyinstitute.edu.sv")
