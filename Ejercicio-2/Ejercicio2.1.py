
# Falto el profe y los compañeros van a armar la clase

# Funcion para obtener al asistente y profesor segun la edadf.
def obtener_compañeros(cantidad_compañeros):
    
    # Creando una lista para almacenar los compañeros
    compañeros = []
    
    # Ejecurtando un ciclo for para pedir los datos de cada compañero
    for i in range(cantidad_compañeros):
        nombre = input(f"Ingresa el nombre del compañero: ")
        edad = int(input(f"Ingresa la edad del compañero: "))
        compañero = (nombre, edad)
        
        compañeros.append(compañero) # añade el compañero a la lista de compañeros
        
    compañeros.sort(key=lambda x: x[1])  # Ordenar por edad, de menor a mayor. La funciona short recibe una funcion lambda que
    # indica que se ordene por el segundo elemento de la tupla (edad)
    asistente = compañeros[0][0]  # El asistente es el primer compañero de la lista, que es el de menor edad
    profesor = compañeros[-1][0]  # El profesor es el ultimo compañero de la lista, que es el de mayor edad
    return asistente, profesor  # Retorna el nombre del asistente y del profesor


asistente, profesor = obtener_compañeros(5)  # Llama a la funcion y guarda el nombre del asistente y del profesor
print(f"El Profesor es {profesor} y el asistente es {asistente}")  # Imprime el nombre del asistente y del profesor



