def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        # No quedan más objetos en la mochila
        return -1
    
    objeto_actual = mochila[indice]
    if objeto_actual == "sable de luz":
        # Encontramos un sable de luz
        return indice
    else:
        # Seguimos buscando
        return usar_la_fuerza(mochila, indice + 1)

# Ejemplo de uso
mochila_ejemplo = ["comida", "agua", "mapa", "sable de luz"]
resultado = usar_la_fuerza(mochila_ejemplo)
if resultado != -1:
    print(f"Encontramos un sable de luz después de sacar {resultado} objetos.")
else:
    print("No se encontró un sable de luz en la mochila.")