def Listar_Informacion(doc):
    titulos=[]
    anyos=[]
    for pelicula in doc["peliculas"]:
        titulos.append(pelicula["titulo"])
        anyos.append(str(pelicula["anno"]))
    return titulos,anyos