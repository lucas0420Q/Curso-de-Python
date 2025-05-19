
#Promedio de duraciones de cursos:
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

# Declaramos las variables de los videos en crudos
crudo_prom = 5
crudo_dalto = 3.5

# Calculando la diferencia entre el curso de Dalto y los otros cursos (Ejercicio A)
diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_curso * 1000 // otros_cursos_max / 10)
diferencia_con_prom = 100 - (dalto_curso / otros_cursos_prom * 100)

# Calculando el porcentaje de tiempo vacio (Ejercicio B)
tiempo_vacio_prom = 100 - (otros_cursos_prom * 1000 // crudo_prom / 10)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)

# Calcular la diferencia si los cursos duraran 10 horas
curso_10_horas = otros_cursos_prom * 100 // dalto_curso / 10
curso_10_horas_dalto = dalto_curso * 100 // otros_cursos_prom / 10

# Mostrando la diferencia entre el curso de Dalto y los otros cursos (Ejercicio A)
# Dividir las respuestas
print("--------------------------------------------------")
print("La diferencia entre el curso de Dalto y el curso mas rapdio es de:", diferencia_con_min, "%")
print("La diferencia entre el curso de Dalto y el curso mas lento es de:", diferencia_con_max, "%")
print("La diferencia entre el curso de Dalto y el promedio de los cursos es de:", diferencia_con_prom, "%")

# Dividir las respuestas
print("--------------------------------------------------")

# Mostrando el porcentaje de tiempo vacio (Ejercicio B)
print("El porcentaje de tiempo vacio es de:", tiempo_vacio_prom, "%")
print("El porcentaje de tiempo vacio en el curso de Dalto es de:", tiempo_vacio_dalto, "%")

# Dividir las respuestas
print("--------------------------------------------------")

# Mostrando la diferencia si los cursos duraran 10 horas
print("Ver 10 horas de curso de Dalto es igual a ver", curso_10_horas, "horas de otros cursos")
print("Ver 10 horas de otros cursos es igual a ver", curso_10_horas_dalto, "horas del curso de Dalto")
# Dividir las respuestas
print("--------------------------------------------------")