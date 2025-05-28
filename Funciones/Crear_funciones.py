
# creando una funcion simple
#def funcion_simple():
#    print("Esta es una funcion simple que no recibe parametros ni devuelve nada")
#ejercutando una funcion simple    
#funcion_simple()

# creando una funcion que recibe parametros
def funcion_con_parametros(parametro1, parametro2):
    print(f"Esta es una funcion que recibe dos parametros: {parametro1} y {parametro2}")

# ejecutando una funcion con parametros
funcion_con_parametros("Hola", "Mundo")


# creando otra funcion que recibe parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()  # Convertimos el sexo a minúsculas para evitar errores de mayúsculas
    # Generamos un saludo basado en el nombre y el sexo
    if sexo == "masculino":
        saludo = f"Hola, Sr. {nombre}"
    elif sexo == "femenino":
        saludo = f"Hola, Sra. {nombre}"
    else:
        saludo = f"Hola, {nombre}"
    return saludo

# ejecutando la funcion saludar
print(saludar("Maria", "nose"))


# Crear un funcion que nos retorne un valor
# def crear_contraseña(num):
#     chars = 'abcdefghij'
#     num_entero = str(num)
#     num = int(num_entero[0]) # Convertimos el primer dígito a entero
#     c1 = num - 2
#     c2 = num
#     c3 = num - 5
#     contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
#     # print(f'La contraseña es: {contraseña}') # Este imprime la contraseña en consola
#     return contraseña  # Este retorna la contraseña para que pueda ser usada en otro lugar

# # ejecutando la funcion crear_contraseña
# password = crear_contraseña(98)
# frase = f"La contraseña generada es: {password}"
# print(frase)  # Imprime la frase con la contraseña generada


# Crear un funcion que nos retorne multiple valores
def crear_contraseña(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0]) # Convertimos el primer dígito a entero
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    # print(f'La contraseña es: {contraseña}') # Este imprime la contraseña en consola
    return contraseña, num  # Este retorna la contraseña para que pueda ser usada en otro lugar

# Desempaquetando los valores retornados por la función
password, Primer_numero = crear_contraseña(98)

# Imprimiendo los valores obtenidos
print(f'La contraseña nueva es: {password}')
print(f'El numero utilizado para crear fue: {Primer_numero}') 