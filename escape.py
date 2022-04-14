import math

radio = input('Ingrese el radio en kilómetros:')
gravedad = input('Ingrese la constante g: ')


velocidad_escape = math.sqrt(2*float(gravedad) * float(radio)*1000)
print(f'La velocidad de escape es : {velocidad_escape:.1f}[m/s]')