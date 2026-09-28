asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
for i in asignaturas:
    notas.append(input(f"Introduce la nota de {i}: "))
print(f"-"*35)
for e in range(5):
    print(f"En {asignaturas[e]} has sacado {notas[e]}")