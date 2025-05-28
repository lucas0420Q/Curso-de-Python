
# Creando un funcion con tres parametros
# def frase(nombre, apellido, edad):
#     return f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años."

# Utilizando keyword arguments para llamar a la función
# frase_con_parametros = frase(nombre="Juan", apellido="Perez", edad=30)
# print(frase_con_parametros)

# Creando la misma función pero con un parámetro opcional y un parámetro por defecto
def frase(nombre, apellido, edad = 25):
    return f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años."

# Utilizando keyword arguments para llamar a la función
frase_con_parametros = frase("Juan", "Perez", 30)
print(frase_con_parametros)