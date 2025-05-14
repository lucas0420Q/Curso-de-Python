
# Creando una lista (Se puede modificar)
lista = ["Lucas Zaracho", "Lino Zaracho", True,  1.75]

# Creando una tupla (No se puede modificar)
tupla = ("Lucas Zaracho", "Lino Zaracho", True,  1.75)

# Esto se puede hacer en una lista
lista[0] = "Lucas"
# lista[0] = "Lucas" # Esto no se puede hacer en una tupla

# Creando un conjunto (Set)

conjunto = {"Lucas Zaracho", "Lino Zaracho", True,  1.75}

print(conjunto)
# Aclaracion, los conjuntos no tienen un orden definido, por lo que no se puede acceder a un elemento en especifico
# Tampoco se pueden repetir elementos

# Creando un diccionario (dict) (La estructura es Key:valor y separado por comas)
diccionario = {
    "nombre": "Lucas Zaracho",
    "apellido": "Zaracho",
    "esta_contento": True,
    "altura": 1.75,
    "datos_duplicado": "Zaracho",
}

print(diccionario["altura"])