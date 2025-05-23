'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    2.3 Casos prácticos de exploración
Descripción:  Cálculo de impuesto

Autor:        Joceline Nicole Ayala Alemán
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

unidadesConsumidas=int(input("Ingrese las unidades consumidas: "))

sinImpuestos=unidadesConsumidas in range(0,101)
impuestoCinco=unidadesConsumidas in range (101,201)
impuestoSiete=unidadesConsumidas >= 201

if sinImpuestos:
    print("No hay impuestos aplicados")
elif impuestoCinco:
    print("El impuesto aplicado es de: ", 0.5*unidadesConsumidas)
elif impuestoSiete:
    print("El impuesto aplicado es de: ", 0.7*unidadesConsumidas)
else:
    print("Error")
