cant=int(input("Digite la cantidad de numesros a ingresear: "))
lista=[]
for i in range(cant):
    lista.append(int(input("Ingrese un numero: ")))
lista.sort()
print(lista[i-1])