def Listar_Informacion(doc):
    lista=[]
    for pelicula in doc["peliculas"]:
        lista.append(pelicula["titulo"]+" "+pelicula["anno"])
    return lista