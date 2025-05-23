'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    2.4 ¡Avanza al siguiente nivel!
Descripción:  Año bisiesto

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

ano = int(input("escribe el año a determinar: "))

if ano in range(1,1000000001):
    if ano % 4 == 0 and ano % 100 != 0 and ano % 400:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
else:
    print("El año no es valido")