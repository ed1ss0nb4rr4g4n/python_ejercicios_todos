asignaturas=["Matemáticas","Física","Química","Historia","Lengua"]
notas=[]
reprobadas=[]
for i in range (len(asignaturas)):
     notas.append(float(input(f"Ingrese la nota de {asignaturas[i]}: ")))
     if notas [i] < 3:
            reprobadas.append(asignaturas[i]) 

if len(reprobadas) == 0:
    print(f"¡Felicidades! Aprobaste todas las asignaturas.")
else:
    print("Las asignaturas que el usuario tiene que repetir son:")
    for i in reprobadas:
        print(f"- {i}")