

# Iniciar el input para pedirle al usuario que ingrese una frase
frase = input("Ingrese una frase y te calculo cuanto tardarias en decirlo: ")

# Calcular la cantidad de palabras separadas por espacios en la frase
palabras = frase.split(" ")

# Calcular la cantidad de palabras en la frase
cantidad_palabras = len(palabras)

# Calcular la cantidad de letras en la frase
velocidad_que_habla = round(len(frase) / 3, 2)
velocidad_que_habla_dalto = round(cantidad_palabras / 3, 2)

if cantidad_palabras > 120:
    print("----------------------------------------------------------------")
    print("Es una frase muy larga, debes resumirla")

print("----------------------------------------------------------------")
print('Dijiste ' + str(cantidad_palabras) + ' palabras en ' + str(velocidad_que_habla) + ' segundos')
print('Dalto tardaria ' + str(velocidad_que_habla_dalto) + ' segundos en decirlo')
print("----------------------------------------------------------------")