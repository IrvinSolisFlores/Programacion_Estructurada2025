import six

def main():
    opcion = True
    inventario_productos = []
    
    while opcion:
        opcion = six.menu_principal()
        
        match opcion:
            case "1":
                six.agregar_producto(inventario_productos)
                six.esperar_tecla()
            
            case "2":
                six.mostrar_productos(inventario_productos)
                six.esperar_tecla()
            
            case "3":
                six.borrar_pantalla()
                print("\n" + "=" * 50)
                print(" BUSCAR PRODUCTO")
                print("=" * 50)
                id_buscar = input("Ingrese ID del producto: ")
                producto = six.buscar_producto(inventario_productos, id_buscar)
                if producto:
                    print("\n" + "-" * 50)
                    print(f"Nombre: {producto[1]}")
                    print(f"Precio: ${producto[2]:.2f}")
                    print(f"Stock crítico: {producto[3]}")
                    print(f"Stock actual: {producto[4]}")
                else:
                    print("\n❌ Producto no encontrado!")
                six.esperar_tecla()
            
            case "4":
                six.actualizar_stock(inventario_productos)
                six.esperar_tecla()
            
            case "5":
                opcion = False
                six.borrar_pantalla()
                print("\n\tSistema cerrado. ¡Hasta pronto!")
            
            case _:
                input("\n\t❌ Opción inválida, presione Enter para continuar...")

if __name__ == "__main__":
    main()