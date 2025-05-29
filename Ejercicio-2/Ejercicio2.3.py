
# Creando un funcion que muestre la serie de Fibonacci entre 0 y el argumento que pasamos

def fibonacci(num):
    fibonacci_lista = [0, 1]
    while fibonacci_lista[-1] <= num:
        fibonacci_lista.append(fibonacci_lista[-2] + fibonacci_lista[-1])
    return fibonacci_lista[:-1]

resultado = fibonacci(34)
print(resultado)
