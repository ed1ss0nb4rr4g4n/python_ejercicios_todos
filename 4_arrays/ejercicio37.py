cant=int(input("Digite la cantidad de numesros a ingresear: "))
lista=[]
for i in range(cant):
    lista.append(int(input("Ingrese un numero: ")))

for i in range(cant):
    for j in range(cant-1):
        if lista[j]>lista[j+1]:
            lista[j],lista[j+1]=lista[j+1],lista[j]
print(f"Lista ordenada: {lista}")