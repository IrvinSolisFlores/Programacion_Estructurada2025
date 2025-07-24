import funciones
from usuarios import usuario
from notas import nota
import getpass


def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            regresar=usuario.registrar(nombre, apellidos, email, password)
            if regresar:
                print(f"{nombre}{apellidos} se registro correctamente con el e-mail{email}")
            else:
                print(f"Por favor intentelo de nuevo.. no fue posible realizar el reistro en este momento...")
            funciones.esperarTecla()
            
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuario=usuario.iniciar_sesion(email, password)
            if lista_usuario:
                menu_notas(lista_usuario[0], lista_usuario[1], lista_usuario[2])
            else:
                print(f"el e-mail y/o contraseña son incorrectos.. por favor intentelo de nuevamente")
            # menu_notas(19,"Dago","Fiscal")
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respueta = nota.crear(usuario_id,titulo,descripcion)
            if respueta:
                print(f"Se creo la nota {titulo} con exito")
            else:
                print(f"No fues posible crear la nota intentelo nuevamente ...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
                print("\n\t Mostrar las Notas")
                print(f"{'id':<10}{'Titulo':<10}{'Descripcion':<10}{'Fecha':<10}")
                print("_"* 60)
                for i in lista_notas:
                    print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
                print("_"*60)
            else:
                print(f"\n\t No Existen nots para este usuaroio")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


