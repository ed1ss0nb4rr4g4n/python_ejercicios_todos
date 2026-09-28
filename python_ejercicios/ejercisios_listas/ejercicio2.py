# Forma numero 1
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for i in asignaturas:
    print(f"Yo estudio {i}")

#Forma numero 2
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print("yo estudio " + ", ".join(asignaturas))