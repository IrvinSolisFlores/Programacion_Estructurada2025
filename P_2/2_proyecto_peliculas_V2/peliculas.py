"""dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
pelicula = {
    "nombre": "",
    "categoria": "",
    "clasificacion": "",
    "genero": "",
    "idioma": ""
}
"""

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
    
def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")
    pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").upper().strip()})
    pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar TODAS las Películas ::.\n")
    resp = input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Característica a Películas ::.\n")
    atributo = input("Ingresa la nueva característica de la película: ").lower().strip()
    valor = input("Ingresa el valor de la característica de la película: ").upper().strip()
    pelicula[atributo] = valor
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")


def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
        respuesta = input("\n\tEstas seguro que deseas borrar alguna caracteristica (Si/No) ?").lower().strip()
        if (respuesta == "si"):    
            atributo = input("\n\tIngresa el nombre de la característica que deseas borrar: ").lower().strip()
            if atributo in pelicula:
                del pelicula[atributo]
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
            else:
                print(f"\n\t\tNo existe ninguna caracteristica con este nombre {atributo}")
        else:
            print("\n\t\t::: OK :::")
    else:
        print("\t..:: No hay películas en el sistema ::..")
def modificarCaracteristica ():
    if len(pelicula) > 0:
        print("\n\t\tModificar caracteristicas")
        for i in pelicula:
            print(f"\n\t\t\t\t\t{i}:{pelicula[i]}")
            resp = input(f"\n\tEstas segur de que quieres modificar el valor de {i} ? (Si/No) :").upper().strip()
            if (resp == "SI"):
                carac = input("\n\tIngresa el nuevo valor :")
                pelicula.update({i:carac})
            else:
                print(f"\n\t\t** se omitio :{i} **")
        print("\n\t\t--La operacion se realizo con exito--")

