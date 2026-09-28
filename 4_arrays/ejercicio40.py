cant=int(input("Digite la cantidad de numesros a ingresear: "))
lista=[]
for i in range(cant):
    lista.append(str(input("Ingrese el producto: ")))
print(f"Lista de compras")
for i in range(cant):
    print(f"{i+1}. {lista[i]}")