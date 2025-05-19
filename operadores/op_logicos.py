
resultado = (10 == 10) & (5 < 10)
# Si ambos son verdaderos, el resultado es verdadero
# Si uno de los dos es falso, el resultado es falso
print('Resultado del AND: ' + str(resultado))

resultado1 = (10 == 10) | (5 > 10)
# Si algunos de los dos es verdadero, el resultado es verdadero
# Si ambos son falsos, el resultado es falso
print('Resultado de OR: ' + str(resultado1))

resultado2 = not (10 == 10)
# Si es verdadero, el resultado es falso
# Si es falso, el resultado es verdadero
print('Resultado de NOT: ' + str(resultado2))
