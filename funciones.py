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
    for 