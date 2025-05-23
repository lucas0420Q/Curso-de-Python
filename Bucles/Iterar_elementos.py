
animales = ['perro', 'gato', 'ratón', 'loro', 'pez']
numeros = (1, 2, 3, 4, 5)

# bucles for para recorrer listas
# for animal in animales:
#     print(animal)


# for numero in numeros:
#     resultado = numero * 10
#     print(resultado)


for numero, animal in zip(numeros, animales):
    print(f'El {animal} tiene {numero} patas')
    
# recorriendo una lista con su índice
# for num in range(1, 11):
#     print(num)
    

# forma correcta de recorrer una lista con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El índice es {indice} y el valor es {valor}')
    

# Usando for con el else
for numero in numeros:
    print(f'El número es {numero}')
else:
    print('No hay más números')
    
# Todo lo anterior funciona igual para tuplas y conjuntos.