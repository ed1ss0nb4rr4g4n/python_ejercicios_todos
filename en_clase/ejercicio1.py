temperaturas=[]
for i in range(7):
    temperaturas.append(int(input(f"Digite la temperatura del dia {i+1} de la semana: ")))
tempAlta=max(temperaturas)
tempBaja=min(temperaturas)
suma=0
for i in temperaturas:
        suma+=i
tempPromedio= suma/7

cantidad=0
for i in range(len(temperaturas)):
    if temperaturas[i]>tempPromedio:
         cantidad+=1

print(f"\nLa temperatura maxima:{tempAlta}\nTemperatura minima:{tempBaja}\nPromedio: {tempPromedio}\nDias por encima del promedio: {cantidad}")