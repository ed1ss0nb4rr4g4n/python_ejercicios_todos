cant=int(input("Digite la cantidad de numesros a ingresear: "))
lista=[]

for i in range(cant):
    lista.append(int(input("Ingrese un numero: ")))
pares=0
impares=0
for i in range(len(lista)):
    if lista[i]%2==0:
        pares+=1
    elif lista[i]%2!=0 or lista[i]==1:
        impares+=1
print(f"""\nPares: {pares} 
Impares: {impares}""")
