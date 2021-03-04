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

def Ejercicio_Libre(director,doc):
    pelicula=[]
    titulo=[]
    trama=[]
    anyo=[]
    precio=[]
    for info in doc["peliculas"]:
        for a in range(len(info)):
            for directores in info["director"]:
                if director==directores:
                    titulo.append(info["titulo"][a])
                    trama.append(info["desc"][a])
                    anyo.append(str(info["anno"])[a])
                    precio.append(str(info["precio"])[a])
                    pelicula=[titulo,trama,anyo,precio]
    return pelicula

