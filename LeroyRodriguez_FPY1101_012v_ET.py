import os
import csv
import random
import time
trabajadores=["Juan Perez", "Maria Garcia", "Carlos Lopez","Ana Martinez", "Pedro Rodriguez", "Laura Hemandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldo1=random.randint(300000,2500000)
sueldo2=random.randint(300000,2500000)
sueldo3=random.randint(300000,2500000)
sueldo4=random.randint(300000,2500000)
sueldo5=random.randint(300000,2500000)
sueldo6=random.randint(300000,2500000)
sueldo7=random.randint(300000,2500000)
sueldo8=random.randint(300000,2500000)
sueldo9=random.randint(300000,2500000)
sueldo10=random.randint(300000,2500000)


def limpiar():
    os.system("cls")

def asignar():
    trabajadores=[["Juan Perez", "Maria Garcia", "Carlos Lopez","Ana Martinez", "Pedro Rodriguez", "Laura Hemandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
                  [sueldo1, sueldo2, sueldo3, sueldo4, sueldo5, sueldo6, sueldo7, sueldo8, sueldo9, sueldo10]]

def guardar():
    with open ("trabajador.csv", mode="w", newline=" ") as archivo:
        guardar=csv.DictWriter(archivo)
        guardar.writerow(trabajadores)
    
def cargar():
    try:
        with open ("trabajador.csv", mode="r") as archivo:
            leer=csv.DictReader(archivo)
            for i in leer:
                trabajadores.append(i)
    except FileNotFoundError:
        print("Archivo no encontrado")

def media(data):
    producto=1
    for valor in data:
        producto*=valor
    return producto**(1/len(data))

def mostrar():
    for trabajador in trabajadores:
        print(trabajador)

        
def main():
    mm=0
    while mm==0:
        print("Bienvenido, que desea hacer?:")
        print("1- Asignar sueldos\n2- Clasificar Sueldos\n3- Ver estadisticas\n4-Reporte de sueldo\n5- Salir del programa")
        try:
            opc=int(input("Ingrese su opcion:\n"))
            if opc==1:
                mostrar()
            elif opc==5:
                print("saliendo del programa")
                mm=54
        except ValueError:
            print("Error ingrese una opcion correcta")
            continue


cargar()
limpiar()
main()