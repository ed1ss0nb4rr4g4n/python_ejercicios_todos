cant=int(input("Digite la cantidad de palabras a ingresar: "))
lista=[]
for i in range(cant):
    lista.append(str(input(f"Escriba la palabra {i+1}: ")))
lista.reverse()
print(lista)
