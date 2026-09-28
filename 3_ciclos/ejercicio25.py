cant=int(input("Ingrese  la cantidad de notas que desea registrar: "))
nt=0
for i in range(cant):
    notas=float(input(f"Ingrese la nota {i+1}: "))
    nt+=notas

promedio=nt/cant
print(f"El promedio de las notas es: {promedio:.2f}")