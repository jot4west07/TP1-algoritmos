def romano_entero(romano):
    if not romano:
        return 0 
    romanos = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    return romanos[romano[0]] + romano_entero(romano[1:])

print("Ingresar numero romano")
romano = input()
print("El numero romano convertido a decimal es: ")
print(romano_entero(romano))



