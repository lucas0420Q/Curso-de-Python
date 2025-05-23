diccionario = {
    'nombre': 'Lucas',
    'apellido': 'Zaracho',
    'edad': 1000,
    'ciudad': 'CABA'
}

# Recorriendo un diccionario con un bucle for y con item().
for key in diccionario.items(): # items() devuelve una lista de tuplas con las claves y los valores del diccionario
    key = key[0] # key[0] es la clave
    value = key[1] # key[1] es el valor
    print(f'La clave es {key} y el valor es {value}')

    