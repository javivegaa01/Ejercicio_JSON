import json
from funciones import *
import os
with open("peliculas.json") as fichero:
    datos=json.load(fichero)

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
        os.system("clear")
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
        os.system("clear")
        print()
        print("El número de peliculas existentes es: %s" % Contar_Informacion(datos))
        print()
    elif opcion==3:
        os.system("clear")
        print()
        p=input("Pelicula: ")
        if validacion_de_pelicula(p,datos)==False:
            print("Tu búsqueda no ha obtenido ningún resultado")
        else:
            print()
            print("---CATEGORIAS---")
            for elem in Buscar_Informacion(p,datos)[0]:
                print(elem)
            print()
            print("---DIRECTOR---")
            for elem in Buscar_Informacion(p,datos)[1]:
                print(elem)
        print()
    elif opcion==4:
        os.system("clear")
        print()
        a=input("Actor: ")
        print()
        print("%s ha participado en las siguientes peliculas:" % a)
        print()
        for elem in Buscar_Informacion_Relacionada(a,datos):
            print("--> ",elem)
        print()
    elif opcion==5:
        os.system("clear")
        d=input("Director: ")
        print()
        print("%s ha participado en %i peliculas: " %(d,len(Ejercicio_Libre(d,datos))))
        print()
        for a in range(len(Ejercicio_Libre(d,datos))):
            for elem in Ejercicio_Libre(d,datos)[a].items():
                print(elem[0],":",elem[1])
            print()
                


        