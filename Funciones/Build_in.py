
numeros = [43, 23, 12, 34, 56]

# El numero mas alto
numeros_mayor = max(numeros)
print(numeros_mayor)

# El numero mas bajo
numeros_menor = min(numeros)
print(numeros_menor)

# Redondear un numero, con la ',2' se indica que se redondee a dos decimales
numero = 3.14559
numero_redondeado = round(numero, 2)
print(numero_redondeado)

# Resultado de un valor booleano, devuelve false si el valor es 0, vacio o None
resultado_booleano_false = bool(0)
print(resultado_booleano_false)

# Resultado de un valor booleano, devuelve true si el valor es diferente de 0 o si enviamos un cadena de texto
resultado_booleano_true = bool("Hola")
print(resultado_booleano_true)

# Retorna true, si todos los valores son verdaderos
resultado_todos_true = all([True, True, True])
print(resultado_todos_true)

# Retorna true, si al menos un valor es verdadero
resultado_al_menos_uno_true = any([False, True, False])
print(resultado_al_menos_uno_true)

# Suma todos los valores de una lista
suma_lista = sum(numeros)  # El segundo argumento es el valor inicial para la suma
print(suma_lista)