import os
"""
List(Array)
son collectiones o conjunto de datos/vslores bajo un mismo nombre para acceder a los valore"""
paises =["Mexico","Brasil","España","Canada"] 
numeros=[23,45,23,8,24]
varios=["hola",3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#recorer una lista e imprimir el contenido
#1era forma
for i in paises:
    print(i)

#2da forma
for i in range (0,len(paises)):#Len es para leer las casillas de las listas
    print(paises[i])

#3ra forma
lista =""
for i in paises:
    lista = lista + f"{i},"
print(lista)

#otra forma

lista =""
for i in range(0,4):
    lista = lista + f"{paises[i]}, "
print(lista)

os.system("cls")

#ordenarlas de manera acendente (de menor a mayor)
print(paises)
print(numeros)
print(varios)

paises.sort()
print(paises)
numeros.sort()
print(numeros)
#varios.sort()
#print(varios)

#Dar la vuelta a las listas pra poder usar esto se necesita primero hacer la primera lista

#varios.reverse()
#print(varios)
paises.reverse()
print(paises)
numeros.reverse()
print(numeros)

#Buscar un elemento dentro de una lista
print("España" in paises)

#para insertar, añadir, agregar un elemento a una lista
os.system("cls")
print(paises)
#1er forma
paises.append("México")
print(paises)

#2da forma
paises.insert(1,"México")
print(paises)

#Borrar, eliminar, suprimir, quitar un elemento de la lista
os.system("cls")
print(paises)

#1er forma
paises.pop(0)
print(paises)

#2da forma
paises.remove("México")
print(paises)

paises.sort()
print(paises)

os.system("cls")

#obtener el indice o la pocicion en la cual se encuentra un elemento
print(paises)

pocicion=paises.index("Canada")
print(pocicion)
paises.pop(pocicion)
print(paises)

#contar el numero de veces que un elemento existe en una lista
os.system("cls")
print(numeros)
cuantas = numeros.count(45)
print(cuantas)
cuantas = numeros.count(23)
print(cuantas)
cuantas = numeros.count(223)
print(cuantas)

#unir el contenido de una lista en otra
os.system("cls")
print(numeros)
numeros2= [100, 200]
print(numeros2)

#crear un programa que una las listas 1 y 2 y imprima 
# el contenido de la lista resultante de forma decendente
numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
