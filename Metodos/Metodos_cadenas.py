
cadena1 = 'Hola soy lucas'
cadena2 = '4234234'

resultado = cadena1.upper()  # Convierte la cadena a mayúsculas

resultado1 = cadena1.lower()  # Convierte la cadena a minúsculas

resultado3 = cadena1.capitalize()  # Convierte la primera letra a mayúscula

resultado4 = cadena1.find('l')  # Busca la posición de la subcadena 'lucas' en cadena1

resultado5 = cadena1.index('l')  # Busca la posición de la subcadena 'l' en cadena1, lanza error si no existe

resultado6 = cadena2.isnumeric()  # Verifica si la cadena es numérica devuelve True y si no devuelve False

resultado7 = cadena1.isalpha()  # Verifica si la cadena es alfabética devuelve True y si no devuelve False (Si tiene espacios devuelve False)

resultado8 = cadena1.count('l')  # Cuenta la cantidad de veces que aparece la letra 'l' en cadena1

resultado9 = len(cadena1)  # Devuelve la longitud de la cadena (cantidad de caracteres)

resultado10 = cadena1.startswith('H')  # Verifica si la cadena empieza con 'H' devuelve True y si no devuelve False

resultado11 = cadena1.endswith('s')  # Verifica si la cadena termina con 's' devuelve True y si no devuelve False

resultado12 = cadena1.replace('Hola', 'Chau')  # Reemplaza la cadena anterior por la nueva cadena y si no existe devuelve la cadena original

resultado13 = cadena1.split(' ')  # Divide la cadena en una lista de palabras separadas por lo que le pases y devuelve una lista

print(resultado13)