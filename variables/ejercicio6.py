segundos=int(input("Ingrese una cantidad en segundos: "))
horas=int(segundos/3600)
restante=int(segundos%3600)
minutos=int(restante/60)
segundos=int(restante%60)

print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")