"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("clear")
paises = ["México","Brasil","España","Canada"]

pais1 = {"nombre":"Mexico",
          "Capital":"CDMX",
          "Poblacion":12000000,
          "idiomas":"Español",
          "Status":True
         }

pais2 = {"nombre":"Brasil",
          "Capital":"Brasilia",
          "Poblacion":14000000,
          "idiomas":"Portugues",
          "Status":True
         }
pais3 = {"nombre":"Canada",
          "Capital":"Otawua",
          "Poblacion":8000000,
          "idiomas":["ingles","Frances"],
          "Status":True
         }

#Dunciones u operaciones con diccionario

print(pais1)
for i in pais1:
    print(f"{i} :{pais1[i]}")

#Agregar un atributo a un dict
pais1["altitud"]=3000

print(pais1)
for i in pais1:
    print(f"{i} :{pais1[i]}")

#quitar un atributo en particular
pais1.pop("Status")
print(pais1)
for i in pais1:
    print(f"{i} :{pais1[i]}")