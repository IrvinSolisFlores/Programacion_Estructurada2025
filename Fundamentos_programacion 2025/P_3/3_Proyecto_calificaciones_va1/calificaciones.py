"""
lista=[
        ["Ruben",10.0,8.9,9.2],
        ["Andrés",10.0,10.0,10.0],
        ["María",10.0,10.0,10.0]
      ] 
"""
import mysql.connector
from mysql.connector import Error


def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="bd_calificaciones"
    )
    return conexion
  except Error as e:
    print(f"El error que se presento es: {e}")
    return None

def menu_principal(): 
    print("\n\t\t..::: Sistema de Gestión de Calificaciones. :::..\n\n\t\t1.- Agregar\n\t\t2.- Mostrar\n\t\t3.- Cálcular Promedios\n\t\t4.- SALIR")
    opcion = input("\n\t\t Elige una opción (1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    conexionBd = conectar()
    if conexionBd != None: 
        print(".:: Agragar Calificaciones ::.")
        nombre=input("Nombre del Alumno: ").upper().strip()
        calificaciones=[]
        for i in range(1,4):
            bandera=True
            while bandera:
                try:
                    #calificaciones.append(float(input(f"Calificaciones {i}: ")))
                    cal=float(input(f"Calificación {i}:"))
                    if cal >= 0 and cal<=10:
                        calificaciones.append(cal)
                        bandera=False
                    else:
                        input("Ingrese en valor comprendido entre 0 y 10: ")
                        esperarTecla()
                except ValueError:
                    input("Ingrese el valor numerico")
                    esperarTecla()
        cursor = conexionBd.cursor()
        sql = ("insert into calificaciones_nombre (nombre_alumno, parcial1, parcial2, parcial3) values (%s, %s, %s, %s);")
        py = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
        cursor.execute(sql, py)
        conexionBd.commit()
        print("Accion realizada con exito ")

    

    """nombre = input("\n\t\tIngrese el nombre del alumno: ")
    calificaciones = []
    for i in range(3):
        calificacion = float(input(f"\n\t\tIngrese la calificación {i+1} de {nombre}: "))
        calificaciones.append(calificacion)
    lista.append([nombre] + calificaciones)
    print(f"\n\t\tCalificaciones de {nombre} agregadas exitosamente.")"""

def mostrar_calificaciones(lista):
    borrarPantalla()
    conexionBd = conectar()
    print("\n\t\t..::: Mostrar Calificaciones :::..\n") 

    if conexionBd != None:
     print(f"{'Nombre':<15}{'Calific.1':<10}{'Calific.2':<10}{'Calific.3':<10}{'Id':<10}")
     print("-"*50)
     cursor = conexionBd.cursor()
     cursor.execute("select * from calificaciones_nombre")
     regitros = cursor.fetchall()
     if regitros != None:
        for fila in regitros:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print("-"*50)   
     else: 
       print("No hay calificaiones en el Sistema")
    else:
        print("La base de datos no se encuentra disponible por el momento porfavor intentelo mas tarde")

def calcular_promedios():
    borrarPantalla()
    conexionBd = conectar()
    if conexionBd != None:
        print(".::Promedios Alumnos::.")
        cursor = conexionBd.cursor()
        cursor.execute("select * from calificaciones_nombre nombre_alumno, parcial1, parcial2, parcial3")
        lista = cursor.fetchall()
        for linea in lista:
            promedio = (linea[1] + linea[2] + linea[3]) /3
        if len(lista) > 0:
            print(f"{'Nombre':<15}{'Promedio':<10}")
            print("-" * 30)
            suma_general = 0
            for fila in lista:
                suma_general += promedio
                print(f"{fila[0]:<15}{promedio:<10}")
            promedio_general = suma_general / len(lista)
            print("-" * 30)
            print(f"El promedio general es: {promedio_general:.2f}")
    else:
        print("No hay calificaciones en la lista")

def buscar(Lista):
    borrarPantalla()
    print("Buscar alumnos")
    if len(Lista) > 0:
        nombre = input("Nombre del alumno que deseas buscar :").upper().strip()
        if nombre in Lista:
            acum = 0
            for fila in Lista:
                try:
                    acum+=1
                    print(f"{"Nombre":<15}{"calificacion 1":>10}{"calificacion 2":>10}{"calificacion 3":>10}")
                    print("_"*30)
                    print(f"{Lista[0]:<15}{Lista[1]:>10}{Lista[2]:>10}{Lista[3]:>10}")
                except ValueError:
                    print("Error el alumno no esta regitrado o no existe")
    else:
        print("No hay ningun alumno registrado")
        esperarTecla()