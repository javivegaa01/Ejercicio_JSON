import json
with open("peliculas.json") as fichero:
    datos=json.load(fichero)
from funciones import *

print("Bienvenido al programa")
print()

while True:
    menu=''' MENÚ:
    1.Listar información
    2.Contar información
    3.Buscar información
    4.Buscar información relacionada
    5.Ejercicio libre
    6.Salir
    '''
    print(menu)
    opcion=int(input("Eliga una opción: "))
    while opcion<1 or opcion>6:
        print("Imposible")
        opcion=int(input("Vuelve a introducir una opción: "))
    if opcion==6:
        break
    elif opcion==1:
        tit,anyo=Listar_Informacion(datos)
        lista=[]
        for elem in Listar_Informacion(datos)[0]:
            lista.append(len(elem))
        print()
        print("---------------------LISTADO DE PELICULAS-----------------------")
        print("  TITULO                                                    AÑO")
        print()
        for elem1,elem2 in zip(tit,anyo):
            print(" ",elem1,elem2.rjust((max(lista)+6)-len(elem1)," "))
        print("----------------------------------------------------------------")
        print()
    elif opcion==2:
        print()
        print("El número de peliculas existentes es: %s" % Contar_Informacion(datos))
        print()
        
            
            