cant=int(input("Digite la cantidad de numesros a ingresear: "))
list=[]
for i in range(cant):
    list.append(int(input("Ingrese un numero: ")))

busca=int(input("Digite el numero a buscar en la lista: "))
for i in range(len(list)):
    list.index(busca)
if list.index(busca):
    print(f"El numero {busca} se encuentra en la posicion {list.index(busca)}")
else:
    print(f"No se encuentra en la lista")
print(*list)