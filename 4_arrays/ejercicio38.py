lista1=[]
lista2=[]
lista3=[]
cant=int(input("Digite la cantidad de elementos a ingresar en dos listas: "))
for i in range(cant):
    lista1.append(int(input("Digite el numero que desea ingresar a la lista 1: ")))
for i in range(cant):
    lista2.append(int(input("Digite el numero que desea ingresar a la lista 2: ")))
    
lista3.extend(lista1+lista2)
print(lista3)