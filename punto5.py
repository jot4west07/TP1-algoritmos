def romano_entero(romano):
    if not romano:
        return 0 
    romanos = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    # romano[0]: obtiene el primer caracter del string romano
    # romanos[romano[0]]: Utiliza ese primer carácter para acceder al valor correspondiente en el diccionario romanos. En este caso, si el primer carácter es 'I', el valor en el diccionario romanos es 1 (ya que 'I': 1 en el diccionario)
    # romano_entero(romano[1:]) llama a la función romano_entero, pero esta vez pasa la subcadena sin el primer caracter. En lugar de procesar todo el string, ahora solo se esta procesando el resto de los caracteres
    # Finalmente, se hace una suma entre el valor del primer carácter y el resultado de la llamada recursiva romano_entero(romano[1:]), hasta la letra elegida
    return romanos[romano[0]] + romano_entero(romano[1:])

print("Ingresar numero romano")
ingreso = input()
romano = ingreso.upper() # Pasar a maysuculas porque la lista de romanos esta en mayusculas
print("El numero romano convertido a decimal es: ")
print(romano_entero(romano))



