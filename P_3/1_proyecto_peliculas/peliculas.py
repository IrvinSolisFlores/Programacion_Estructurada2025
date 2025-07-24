import mysql.connector
from mysql.connector import Error

#Dict u objeto los atributos (nombre,categoria,clasificacion,genero,idioma) 

# pelicula={
#            "nombre":"",
#            "categoria":"",
#            "clasificacion":"",
#            "genero":"",
#            "idioma":""
#          }

pelicula={}

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t... Oprima cualquier tecla para continuar ...") 

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="bd_peliculas"
    )
    return conexion
  except Error as e:
    print(f"El error que se presento es: {e}")
    return None

def crearPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
      print("\n\t\t.:: Crear Películas ::. \n")
      pelicula.update({"nombre":input("\nIngresa el nombre: ").upper().strip()})
    # pelicula["nombre"]=input("\nIngresa el nombre: ").upper().strip()
      pelicula.update({"categoria":input("\nIngresa la categoría: ").upper().strip()})
      pelicula.update({"clasificacion":input("\nIngresa la clasificación: ").upper().strip()})
      pelicula.update({"genero":input("\nIngresa el genero: ").upper().strip()})
      pelicula.update({"idioma":input("\nIngresa el idioma: ").upper().strip()})
      ##### Sql para BD
      cursor=conexionBD.cursor()
      sql="insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values ( %s, %s, %s, %s, %s)"
      val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")

def mostrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    cursor=conexionBD.cursor()
    sql="select * from peliculas"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
    else:
      print("\t ..:: No hay películas en el sistema ::. ")

def buscarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    nombre=input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
    else:
      print("\t ..:: Las películas a buscar no estan en el sistema ::. ")      

def borrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
    else:
      print("\t ..:: Las películas a buscar no estan en el sistema ::. ")
      
def modificarPelicula():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("Modificador de peliculas")
        nombre = input("Ingresa el nombre de la pelicula a modificar: ").upper().strip()
        cursor = conexionBD.cursor()
        codigo = "SELECT * FROM peliculas WHERE nombre = %s"
        cursor.execute(codigo, (nombre,))
        registro = cursor.fetchone()

        if registro:  # Verifica si se encontró un registro
            print("...:::Ingresa los nuevos parametros:::--")
            pelicula = {}
            pelicula.update({"nombre": input("\nIngresa el nombre: ").upper().strip()})
            pelicula.update({"categoria": input("\nIngresa la categoría: ").upper().strip()})
            pelicula.update({"clasificacion": input("\nIngresa la clasificación: ").upper().strip()})
            pelicula.update({"genero": input("\nIngresa el genero: ").upper().strip()})
            pelicula.update({"idioma": input("\nIngresa el idioma: ").upper().strip()})
            
            sql = """UPDATE peliculas 
                     SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s  
                     WHERE nombre = %s"""
            val = (
                pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"],
                pelicula["genero"], pelicula["idioma"], nombre
            )
            cursor.execute(sql, val)
            conexionBD.commit()
            print("Operación realizada con éxito")
        else:
            print("\t..:: La película a modificar no está en el sistema ::..")