"""
crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones:
1.-sin estructuras de control
2.-sin funciones
"""
numero_usuario = int(input("inserta el numero de la tabla de multiplicacion :"))
tabla = numero_usuario * 1
print (f"{numero_usuario} x 1 = {tabla}")
tabla = numero_usuario * 2
print (f"{numero_usuario} x 2 = {tabla}")
tabla = numero_usuario * 3
print (f"{numero_usuario} x 3 = {tabla}")
tabla = numero_usuario * 4
print (f"{numero_usuario} x 4 = {tabla}")
tabla = numero_usuario * 5
print (f"{numero_usuario} x 5 = {tabla}")
tabla = numero_usuario * 6
print (f"{numero_usuario} x 6 = {tabla}")
tabla = numero_usuario * 7
print (f"{numero_usuario} x 7 = {tabla}")
tabla = numero_usuario * 8
print (f"{numero_usuario} x 8 = {tabla}")
tabla = numero_usuario * 9
print (f"{numero_usuario} x 9 = {tabla}")
tabla = numero_usuario * 10
print (f"{numero_usuario} x 10 = {tabla}")

#vercion 2


numero_tabla = int(input("Ingresa el Numero de la tabla que desas rrealizar: "))
for i in range (1,10+1):
    tablav2 = numero_tabla * i
    print (f"{numero_tabla} x {i} = {tablav2}") 

#version 3
num = int(input("Ingresa el Numero de la tabla que desas rrealizar: "))
def tablas (numero):
    num = numero
    respuesta = "" 
    for i in range (1, 11):
        multi = num + 1
        respuesta = f"\t{num} x {i} = {multi}\n"
        return respuesta
