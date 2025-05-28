
numeros = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]

# Creando una funcion lambda para multiplicar por 2
multiplicar_por_2 = lambda x: x * 2
print(multiplicar_por_2(5))  # Imprime 10

# Creando una funcion comun que diga si un numero es par
# def es_par(num):
#     if num % 2 == 0:
#         return True

# Usando filter con una funcion comun 
# numeros_pares = filter(lambda numero: numero % 2 ==0, numeros)

# Usando filter con una funcion lambda
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)

print(list(numeros_pares)) # imprime la lista de numeros pares
