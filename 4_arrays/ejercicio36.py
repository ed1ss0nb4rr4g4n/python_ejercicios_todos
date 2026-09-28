# cant=int(input("Digite la cantidad de numesros a ingresear: "))
# lista=[]
# lista_filtrada=[]
# for i in range(cant):
#     lista.append(int(input("Ingrese un numero: ")))

# for i in lista:
#     if i not in lista_filtrada:
#         lista_filtrada.append(i)
# lista_filtrada.sort()
# print(f"Lista de numeros sin repetir: {lista_filtrada}")

# forma 2
cant=int(input("Digite la cantidad de numesros a ingresear: "))
lista=[]

for i in range(cant):
    lista.append(int(input("Ingrese un numero: ")))

lista_filtrada=list(set(lista))
lista_filtrada.sort()
print(f"Lista de numeros sin repetir: {lista_filtrada}")

