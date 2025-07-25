"""
lista=[
        ["Ruben",10.0,8.9,9.2],
        ["Andrés",10.0,10.0,10.0],
        ["María",10.0,10.0,10.0]
      ] 
"""
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal(): 
    print("\n\t\t..::: Sistema de Gestión de Calificaciones. :::..\n\n\t\t1.- Agregar\n\t\t2.- Mostrar\n\t\t3.- Cálcular Promedios\n\t\t4.- SALIR")
    opcion = input("\n\t\t Elige una opción (1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
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
    lista.append([nombre] + calificaciones)
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
    print("\n\t\t..::: Mostrar Calificaciones :::..\n") 
    if len(lista)>0:
     print(f"{"Nombre":<15}{"Calific.1":<10}{"Calific.2":<10}{"Calific.3":<10}")
     print("-"*50)
     for fila in lista:
        print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
     print("-"*50)
     print(f"Son {len(lista)} alumnos")
    else: 
       print("No hay calificaiones en el Sistema")

def calcular_promedios(Lista):
    borrarPantalla()
    print(".::Promedios Alumnos::.")
    if len(Lista) > 0:
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print("-" * 30)
        suma_general = 0
        for fila in Lista:
            promedio = (fila[1] + fila[2] + fila[3]) / 3
            suma_general += promedio
            print(f"{fila[0]:<15}{promedio:<10.2f}")
        promedio_general = suma_general / len(Lista)
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