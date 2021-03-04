def Listar_Informacion(doc):
    titulos=[]
    anyos=[]
    for info in doc["peliculas"]:
        titulos.append(info["titulo"])
        anyos.append(str(info["anno"]))
    return titulos,anyos

def Contar_Informacion(doc):
    titulos=[]
    for info in doc["peliculas"]:
        titulos.append(info["titulo"])
    return len(titulos)

def Buscar_Informacion(pelicula,doc):
    for info in doc["peliculas"]:
        if info["titulo"]==pelicula:
            categoria=info["categoria"]
            director=info["director"]
    return categoria,director

def Buscar_Informacion_Relacionada(actor,doc):
    lista_peliculas=[]
    for info in doc["peliculas"]:
        for actores in info["actores"]:
            if actor==actores["nombre"]:
                lista_peliculas.append(info["titulo"])
    return lista_peliculas

#def Ejercicio_Libre():
    #return

