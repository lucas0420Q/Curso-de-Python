
ingreso_mensuales = 50000
gastos_mensuales = 20000

if ingreso_mensuales > 10000:
    if ingreso_mensuales - gastos_mensuales > 5000:
        print("Estas bien enconomicamente y ahorrando")
    else:
        print("Estas gastando de mas debes cuidar tus gastos")
elif ingreso_mensuales > 5000:
    print("Estas bien economicamente para latinoamerica")
elif ingreso_mensuales > 2000:
    print("Estas bien economicamente para tu pais")
elif ingreso_mensuales > 1000:
    print("Estas bien economicamente para tu ciudad")
else:
    print("No estas bien economicamente")   