
# Forma no optima de sumar numeros
def sumar_numeros(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = sumar_numeros([1, 2, 3, 4, 5])
print(f"La suma de los numeros es: {resultado} De forma no optima")

# Forma optima de sumar numeros, ulizando el operador *args
def sumar_numeros_optimo(*numeros): # Usando * para recibir un número variable de argumentos
    return sum(numeros) # Esta función usa la función sum() para sumar todos los números
resultado_optimo = sumar_numeros_optimo(1, 2, 3, 4, 5)
print(f"La suma de los numeros es: {resultado_optimo} De forma optima")

print("--------------------------------------------------")

# Otro ejemplo de uso de *args, con dos parametros
def mostrar_datos(nombre, *numeros):
    return f'{nombre}, la suma de los numeros es: {sum(numeros)}'
resultado_datos = mostrar_datos("Juan", 1, 2, 3, 4, 5)
print(resultado_datos)
