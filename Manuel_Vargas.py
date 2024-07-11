import os 
import time
import csv
import random 
opcion = 0
def borrar():
    os.system("cls")

def mi_numero_azar():
    n=random.randint(300.000,2500000)
    return n


azar=mi_numero_azar()

def leer_datos_archivo(archivo):

        lista_trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]   

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldo = int(azar)

borrar()
while opcion <5:
    
    print("\nDATOS")
    print("\t1. Asignar sueldos aleatorios")
    print("\t2. Clasificar sueldos")
    print("\t3. Ver estadísticas.")
    print("\t4. Reporte de sueldos")
    print("\t5. Salir del programa")
    opcion=int(input("Ingrese una opciòn [1-5]:  "))
    if opcion>=1 and opcion<=5:
         print("sueldos asginados")
         print(input(""))
         borrar()
    if opcion>=2  and opcion<=5: 
         print("\tSueldos menores a $800.000 TOTAL: 2")
         print("")
         print("\tNombre empleado \tSueldo")
         print(f"\tJuan Pérez        \t{sueldo}")
         print(f"\tMaría García      \t{azar}")
         print("")
         print("Sueldos entre $800.000 y $2.000.000")
         print("TOTAL: 2")
         print("")
         print("\tNombre empleado \tSueldo")
         print(f"\t")
         print(input("coloque ENTER para salir..."))
    if opcion>=3 and opcion<=5:
         print
    if opcion>=3 and opcion<=5:
        print
    if opcion>=4 and opcion<=5:
        print(input())
    if opcion>=5 and opcion<=5:
         print