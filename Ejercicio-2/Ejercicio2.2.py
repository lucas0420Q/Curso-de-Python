
# creando una funcion que nos devuelve los numeros primos
# Entre 0 y el argumento que pasamos

def es_primo(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3, num + 1):
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)
    return primos

resultado = primos_hasta(13)
print(resultado)

