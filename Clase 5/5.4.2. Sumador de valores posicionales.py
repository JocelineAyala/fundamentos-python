'''
Clase:        Clase 8
Tema:         Estructuras Iterativas
Ejercicio:    5.4.1 Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus digitios hasta que quede un solo digito.

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

while True:
    num = input("Ingresa un número: ")
    
    if num.isdigit():
        conversion = int(num)
        if 1 <= conversion <= 1000000000:
            break
        else:
            print("Número ingresado está fuera del rango")
    else:
        print("El valor ingresado no es un número")


print(f"Proceso de reducción para {num}:")
while len(num) > 1:
    suma = 0
    for i in num:
        suma += int(i)
    print(f"{num} = {suma}")
    num = str(suma)

print(f"El resultado final es: {suma}")