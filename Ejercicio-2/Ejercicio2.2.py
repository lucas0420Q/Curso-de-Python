
# creando una funcion que nos devuelve los numeros primos
# Entre 0 y el argumento que pasamos

def es_primo(num):  # Define una función que recibe un número como parámetro
    for i in range(2, num - 1):  # Itera desde 2 hasta num-2 (no incluye num-1)
        if num % i == 0:  # Si num es divisible por i (resto de la división es 0)
            return False  # Retorna False porque encontró un divisor, no es primo
    return True  # Si no encontró divisores, retorna True (es primo)

def primos_hasta(num):  # Define función que encuentra primos hasta un número dado
    primos = []  # Crea una lista vacía para almacenar los números primos
    for i in range(3, num + 1):  # Itera desde 3 hasta num (incluye num)
        resultado = es_primo(i)  # Llama a la función es_primo para verificar si i es primo
        if resultado == True:  # Si el resultado es True (es primo)
            primos.append(i)  # Agrega el número i a la lista de primos
    return primos  # Retorna la lista completa de números primos encontrados

resultado = primos_hasta(13)  # Llama a la función para encontrar primos hasta 13
print(resultado)  # Imprime la lista de números primos encontrados
