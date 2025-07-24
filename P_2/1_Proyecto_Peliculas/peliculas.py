peliculas = {}


def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("Precione una tecla para continuar...")
    
def agregarPeliculas():
    borrarPantalla()
    print("\n\t\tAgregar pelicula")
    peliculas.append(input("\nIngrese el nombre :").upper().strip())
    print("\n\t\tLA OPERACION SE REALIZO CON EXITO")
    
    
def consultarPeliculas ():
    borrarPantalla()
    print("\n\t\tConsultar peliculas")
    
    if len(peliculas)>0:
        for i in range (0,len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")
    else:
        print("\n\t\tNo hay peliculas en el sistema")
        
def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\tLimpiar/borrar todas las peliculas")
    resp = input("¿Deseas borrar las peliculas?(Si/No)").lower
    
    if resp == "si":
        peliculas.clear()
        print("\n\t\t la operacion se realizo con exito")
        
        
        
def buscarPeliculas():
    borrarPantalla()
    print("\n\t\tBuscar una las peliculas")
    pelicula_buscar = input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t No hay nunguna pelicula con este nombre")
    else:
        encontro = 0 
        for i in range(0,len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                print(f"\n\t La pelicula{pelicula_buscar}si latenemos y esta casillero: {i+1} ")
                encontro += 1
        print(f"\n\tTenemos {encontro} peliculas(s) con este titulo")
        
        
def modificarPeliculas():
    borrarPantalla()
    print("\n\t\tModificar una las peliculas")
    pelicula_buscar = input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t No hay nunguna pelicula con este nombre")
    else:
        encontro = 0 
        for i in range(0,len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                resp = input("¿Deseas actualizar la pelicula? (Si/No)").lower().strip()
                if resp== "si":
                    peliculas[i]=input("\n\tIntrodusca/tecle el nuevo valos de la pelicula").upper().strip()
                    
                    print(f"\n\t La pelicula{peliculas[i]}si latenemos en el casillero: {i+1} ")
                    encontro += 1
        print(f"\n\tSe ctualizaron {encontro} peliculas(s) con este Titulo")
def eliminarPeliculas():
    borrarPantalla()
    print("\n\t\tEliminar una de las peliculas")
    pelicula_buscar = input("ingresa el nombre de la pelicula a eliminar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t No hay nunguna pelicula con este nombre")
    else:
        encontro = 0
        for i in range(0,len(peliculas)):
                resp = input("¿Deseas eliminar la pelicula? (Si/No)").lower().strip()
                if resp== "si":
                    peliculas.pop(i)

                    print(f"\n\t La pelicula que se borro es {pelicula_buscar} de la casilla: {i+1} ")
                    print("::La operacion se realizo con exito")
        
def agregarCaracteristicaspeliculas():
    print("\n\t\t Agregar una caracteristica a la Pelicula\t\n")
    atributo=input("\n\t\tIngresa el nombre de la nueva caracteristica").lower().strip()
    valor_atributo=("\n\t\tIngresa el valor del nuevo atributo")
    peliculas.update({atributo:valor_atributo})
    peliculas [atributo] = valor_atributo
    print("\n\t\t La operacion se realiso con exito")


def modificarCaracteristica ():
    print("\n\t\tModificar caracteristicas")
    for i in peliculas:
        print(i)
        resp = input("Estas segur de que quieres modificar este valor ? (Si/No)").lower().strip()
        if (resp == "si"):
            carac = input("Ingrsa el nuevo valor :")
            peliculas.update({i:carac})