
frutas = ["manzana", "pera", "naranja", "kiwi", "sandia"]
cadena = "Hola mundo"
numeros = [1, 2, 3, 4, 5]

# evitando que se ejecute el resto del bucle cuando se cumple una condición con el continue
# el continue se usa para saltar a la siguiente iteración del bucle
# for fruta in frutas:
#     if fruta == "naranja":
#         continue
#     print(f"Encontré una {fruta}!")
    
# el break se usa para salir del bucle
for fruta in frutas:
    print(f"Encontré una {fruta}!")
    if fruta == "naranja":
        break
print("No encontré una naranja")

# Para recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
# For en una sola línea de codigo (Duplicando los números)
# Esta forma de escribir el for es conocida como comprensión de listas (list comprehension)
numeros_duplicados = [numero * 2 for numero in numeros]
print(numeros_duplicados)

