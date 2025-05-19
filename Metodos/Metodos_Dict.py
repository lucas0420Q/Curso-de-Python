diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
}

# Devuelve las claves (Tambien sirve para iterar)
claves = diccionario.keys()

# Devuelve el valor que le pasemos en el GET
claves1 = diccionario.get("ciudad")

# ELiminando todos los elementos del diccionario
#diccionario.clear()

# Eliminar un elemento especifico del diccionario 
diccionario.pop("nombre") # Elimina el elemento que le pases, si no existe lanza error

# Onteniendo un elemento dict_items iterables
claves2 = diccionario.items()

print(claves2)