'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    2.3 Casos prácticos de exploración
Descripción:  Contraseña segura

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

contra = input("Escribe tu contraseña para verificar que es segura: ")


cantidadContra = len(contra)
num = False
mayuscula = False

for char in contra: 
    if char.isdigit():
        num = True

for char in contra:
    if char.isupper():
        mayuscula = True

if cantidadContra and num and mayuscula:
    print("Su contraseña es segura")
else:
    print("Su contraseña no es segura")
