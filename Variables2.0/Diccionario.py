
# Creando u diccionario con dict()
diccionario = dict(nombre='Lucas', apellido='Zaracho', edad=1000, ciudad='CABA')

# Creando u diccionario con frozenset()
diccionario1 = frozenset({'nombre': 'Lucas', 'apellido': 'Zaracho', 'edad': 1000, 'ciudad': 'CABA'}) # Frozenset es un diccionario inmutable, permite crear diccionarios dentro de otros diccionarios

# Creando un diccionario con {}
diccionario2 = {'nombre': 'Lucas', 'apellido': 'Zaracho', 'edad': 1000, 'ciudad': 'CABA'}

# creando un diccionario con fromkeys()
diccionario3 = dict.fromkeys(['nombre', 'apellido', 'edad', 'ciudad']) # fromkeys() crea un diccionario con las claves y el valor que se le pase como segundo argumento


print(diccionario3)