def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        # No quedan más objetos en la mochila
        return -1 # la función devuelve -1 para indicar que no se encontró el objeto en la mochila
    
    objeto_actual = mochila[indice]
    if objeto_actual == "sable de luz":
        # Encontramos un sable de luz
        return indice # indice es el objeto actual en la mochila
    else:
        # Seguimos buscando
        return usar_la_fuerza(mochila, indice + 1) # indice+1 para pasar al siguiente objeto 

# Ejemplo de uso
mochila_ejemplo = ["comida", "agua", "mapa", "sable de luz"]
resultado = usar_la_fuerza(mochila_ejemplo)
if resultado != -1: # si resultado es distinto a -1 se encotro el sables
    print(f"Encontramos un sable de luz después de sacar {resultado} objetos.")
else:
    print("No se encontró un sable de luz en la mochila.")