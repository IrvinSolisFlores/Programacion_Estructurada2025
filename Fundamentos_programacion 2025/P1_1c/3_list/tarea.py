import os
#1er caso

os.system("cls")
#2do caso

palabras = ["UTD","2023","Logo","TI","2c-clasica"]
palabra_buscar = input("Dame la palabra a buscar :")
if palabra_buscar in palabras:
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista")


os.system("cls")
encontro = False
pociciones = []
cuantas = 0
for i in palabras:
    if i == palabra_buscar:
        encontro = True
        cuanta += 1
        pociciones.append(palabras.index(i))
if encontro == True: #Forma simplificada siempre y cuando sea true solo poner if encontro:
    print("Si encontro la palabra en la lista")
    print(f"cuantas son {cuanta}")
    print(f"pociciones {pociciones}")
else:
    print("Si encontro la palabra en la lista")


agenda=[
    ["carlos","6181234567"]
    ["Carlos v","6182381587"]
    ["Carlos vl","618234534587"]
]
print(agenda)

for i in agenda:
    print(i)

for r in range (0,3):
    for c in range (0,2):
        print(agenda [r] [c])

lista = ""
for r in range (0,3):
    for c in range (0,2):
        listav +=f"{agenda [r] [c]}"