
# Creando un conjunto con set()
conjunto = set(['lucas','Zaracho', 1000])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['lucas','Zaracho', 1000]) # Frozenset es un conjunto inmutable, permite crear conjuntos dentro de otros conjuntos
conjunto2 = {conjunto1, 'Lucas', 1000}

# Mostrando el resultado
print(conjunto2)


# Teoria de conjuntos
conjunto = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Verificando si un conjunto es un subconjunto de otro
resultado = conjunto2.issubset(conjunto) # la funcion issubset() devuelve True si el conjunto es un subconjunto del otro
resultado2 = conjunto2 <= conjunto # la funcion <= devuelve True si el conjunto es un subconjunto del otro

# Verificando si un conjunto es un superconjunto de otro
resultado3 = conjunto2.issuperset(conjunto) # la funcion issuperset() devuelve True si el conjunto es un superconjunto del otro
resultado4 = conjunto2 > conjunto # la funcion <= devuelve True si el conjunto es un superconjunto del otro

# Verificar si hay un dato en comun entre los conjuntos
resultado5 = conjunto2.isdisjoint(conjunto) # la funcion isdisjoint() devuelve True si no hay elementos en comun entre los conjuntos

print(resultado5)

