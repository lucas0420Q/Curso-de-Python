
# Creando una lista
lista = list([34,43,53,54])

# contando la cantidad de elementos de la lista
resultado = len(lista)  # Devuelve la longitud de la lista (cantidad de elementos)

# Agregar un elemento a la lista
lista.append(55)  # Agrega un elemento al final de la lista

# Agregar un elemento en una posición específica
lista.insert(1, 'Qtal')  # Agrega un elemento en la posición que le pases

# Agregar varios elementos a la lista
lista.extend([True, False])  # Agrega varios elementos al final de la lista

# Eliminar un elemento de la lista (Por su indice)
lista.pop(-1)  # Elimina el elemento en la posición que le pases, si no le pasas nada elimina el último elemento. Tambien tenes la
# opcion de poner -1 para eliminar el último elemento y asi sucesivamente.

# Remover un elemento de la lista (Por su valor)
lista.remove('Qtal')  # Elimina el elemento que le pases, si no existe lanza error

# Eliminar todos los elementos de la lista
#lista.clear()  # Elimina todos los elementos de la lista

# Ordenar la lista
lista.sort()  # Ordena la lista de menor a mayor, no acepta cadenas de texto. Si usamos el parametro (reverse=True) la ordena en reversa

# Invertir la lista
lista.reverse() # Invierte los elementos de la lista





print(lista)