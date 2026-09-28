diccionario={}
cant=int(input(f"Ingrese la cantidad de estudiantes que desea registrar: "))
for i in range(cant):
    diccionario.update({int(input(f"Digite el codigo del estudiante: ")): str(input(f"Digite el nombre del estudiante: "))})

for i,e in diccionario.items():
    print(f"{i} -> {e}")