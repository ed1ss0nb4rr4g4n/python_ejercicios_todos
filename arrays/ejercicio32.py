
cant=int(input("Digite la cantidad de numeros que desea ingresar: "))
calificaciones=[]

for i in range(cant):
    calificaciones.append(float(input("Digite la calificacion: ")))
    sum=0
for i in range(len(calificaciones)):
    sum+=calificaciones[i]
promedio=sum/cant
print(promedio)