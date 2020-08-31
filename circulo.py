from math import pi

def area_circulo(r):
    if type(r) not in [int, float]:
        raise TypeError ("El radio debe ser un número real no negativo")
    
    if r < 0:
        raise ValueError("El radio no puede ser negativo.")
    return pi*(r**2)