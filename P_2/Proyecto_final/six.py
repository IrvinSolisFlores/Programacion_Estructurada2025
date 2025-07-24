import os

def borrar_pantalla():
    
    os.system('cls')

def esperar_tecla():
    
    input("\nPresione cualquier tecla para continuar...")

def menu_principal():
    
    borrar_pantalla()
    print("\n" + "=" * 50)
    print(" SISTEMA DE GESTIÓN DE INVENTARIO - NEGOCIO SIX")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar stock")
    print("5. Salir")
    return input("\nSeleccione una opción: ")

def agregar_producto(inventario):
    borrar_pantalla()
    print("\n" + "=" * 50)
    print(" AGREGAR NUEVO PRODUCTO")
    print("=" * 50)
    
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    id_producto = input("ID/Código de barras: ")
    stock_critico = int(input("Stock crítico: "))
    stock_actual = int(input("Stock actual: "))
    
    nuevo_producto = [
        id_producto,
        nombre,
        precio,
        stock_critico,
        stock_actual
    ]
    
    inventario.append(nuevo_producto)
    print(f"\n✅ Producto '{nombre}' agregado exitosamente!")

def mostrar_productos(inventario):
    borrar_pantalla()
    print("\n" + "=" * 90)
    print(" INVENTARIO COMPLETO")
    print("=" * 90)
    print("ID/Código\tNombre\t\tPrecio\t\tStock Crítico\tStock Actual")
    print("-" * 90)
    
    for producto in inventario:
        print(f"{producto[0]}\t{producto[1][:15]}\t${producto[2]:.2f}\t\t{producto[3]}\t\t{producto[4]}")
    
    print("=" * 90)


def actualizar_stock(inventario):
    borrar_pantalla()
    print("\n" + "=" * 50)
    print(" ACTUALIZAR STOCK DE PRODUCTO")
    print("=" * 50)
    #sdfnhslkeffffffseeeeensehfkñlshdnklfhskñhfjeskjkljdfjsklekljfjkskldjfksjeklfjkskjelfjseflksjkl
    id_buscar = input("Ingrese ID del producto: ")
    producto = buscar_producto(inventario, id_buscar)## Aqui si da error tira paro esque ne faltaba
    #Lo de buscar el producto nomas a la funcion le pondes ese nombre de buscar_producto
    
    if producto:
        print(f"\nProducto encontrado: {producto[1]}")
        print(f"Stock actual: {producto[4]}")
        nuevo_stock = int(input("Ingrese nuevo stock: "))
        producto[4] = nuevo_stock
        print("\n✅ Stock actualizado correctamente!")
    else:
        print("\n❌ Producto no encontrado!")