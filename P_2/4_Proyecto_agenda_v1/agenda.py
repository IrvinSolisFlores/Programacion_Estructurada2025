def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("Presione una tecla para continuar...")

def agregar_contacto(agenda):
    borrarPantalla()
    print("\t\t\t.::: Agregar Contacto :::.")
    print("=" * 60)
    nombre = input("\t\tIngrese el nombre del contacto: ").upper().strip()
    
    if nombre in agenda:
        print("Ya existe")
    else:
        tel=input("Telefono: ").upper().strip()
        email=input("Email: ").upper().strip()
        agenda[nombre] = [tel, email]
        print("=" * 60)
        print("Accion realizada con Exito")
        
def mostrar_contactos(agenda):
    borrarPantalla()
    if not agenda:
        print("=" * 60)
        print(f"\t\tNo hay contactos")
        print("=" * 60)
    else:
        print("\t\t\t.::: Agenda :::.")
        print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
        print("=" * 60)
        for nombre in agenda:
            tel, email = agenda[nombre]
            print(f"{nombre:<15} {tel:<15} {email:<15}")
        print("=" * 60)
        
def buscar_contacto(agenda):
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto a buscar: ").upper().strip()
    if buscar in agenda:
        persona = agenda[buscar]
        print("=" * 60)
        print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
        print(f"{buscar:<15} {persona[0]:<15} {persona[1]:<15}")
        print("=" * 60)
    else:
        print("=" * 60)
        print("No existe el contacto... Vuelva a intentarlo por favor")
        
#def modificar_contacto(agenda):
 #   borrarPantalla()
 #   print("\n\t.:: Modificar Característica de un contacto ::.\n")
  #  buscar = input("Ingrese el nombre de la persona que quiere modificar: ").upper().strip()
    
  #  if buscar in agenda:
  #      persona = agenda[buscar]
  #      print(f"\n\t*** Los datos de {buscar} son: ***\n")
  #      print(f"\n\t\tTelefono: {persona[0]}")
  #      print(f"\n\t\tEmail: {persona[1]}")
        
  #      dato = input("\nIngresa el nombre de la característica que deseas modificar (Telefono/Email): ").upper().strip()
        
#      if dato == "TELEFONO":
#         nuevo_valor = input("Ingresa el nuevo numero telefonico: ").upper().strip()
#            persona[0] = nuevo_valor
"""            print("La operacion se realizo con exito")
        elif dato == "EMAIL":
            nuevo_valor = input("Ingresa el nuevo email: ").upper().strip()
            persona[1] = nuevo_valor
            print("=" * 60)
            print("La operacion se realizo con exito")
        else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("-" * 60)
        print("\t*** No esta esa persona en la agenda ***")"""
def modificar_contacto(agenda):
    borrarPantalla()
    print("📝 Modificar Contactos...")
    if not agenda:
        print("⚠️ No hay contactos en la Agenda")
    else:
        nombre = input("🔍 Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print("📌 Valores Actuales")
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]}\n📧 E-mail: {agenda[nombre][1]}")
            resp = input("❓ ¿Deseas cambiar los valores? (Si/No) ").lower().strip()
            if resp == "si":
                tel = input("📞 Nuevo Teléfono: ").upper().strip()
                email = input("📧 Nuevo E-mail: ").lower().strip()
                agenda[nombre] = [tel, email]
                print("✅ Acción realizada con éxito")
            else:
                print("🚫 Modificación cancelada")
        else:
            print("❌ Este contacto no existe")

    
"""def borrar_contacto(agenda):
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto que desea borrar: ").upper().strip()
    if buscar in agenda:
        resp = input(f"Se encontro a {buscar}, deseas eliminarla de la agenda (Si/No)?: ").upper().strip()
        if resp == "SI":
            del agenda[buscar]
        print("-" * 60)
        print("La operacion se realizo con exito")
    else:
        print("=" * 60)
        print("No existe el contacto... Vuelva a intentarlo por favor")"""
def borrar_contacto(agenda):
    borrarPantalla()
    print("🗑️ Eliminar Contactos...")
    if not agenda:
        print("⚠️ No hay contactos en la Agenda")
    else:
        nombre = input("🔍 Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print("📌 Valores Actuales")
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]}\n📧 E-mail: {agenda[nombre][1]}")
            resp = input("❓ ¿Deseas eliminar este contacto? (Si/No) ").lower().strip()
            if resp == "si":
                agenda.pop(nombre)
                print("✅ Contacto eliminado con éxito")
            else:
                print("🚫 Eliminación cancelada")
        else:
            print("❌ Este contacto no existe")
