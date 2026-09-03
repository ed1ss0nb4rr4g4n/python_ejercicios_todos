cant = int(input("Digite la cantidad de números a ingresar: "))
print("PASO 1 - Cantidad ingresada:", cant)

lista = []
print("PASO 2 - Lista creada:", lista)

for i in range(cant):
    print("PASO 3 - Iteración para ingresar número:", i)
    
    numero = int(input("Ingrese un número: "))
    print("PASO 4 - Número ingresado:", numero)
    
    lista.append(numero)
    print("PASO 5 - Lista después de agregar:", lista)


print("PASO 6 - Comienza el ordenamiento")
print("Lista inicial:", lista)

for i in range(cant):
    print("PASO 7 - Vuelta número:", i + 1)
    
    for j in range(cant - 1):
        print("PASO 8 - Comparando posiciones:", j, "y", j + 1)
        print("Valores:", lista[j], "y", lista[j + 1])
        
        if lista[j] > lista[j + 1]:
            print("PASO 9 -", lista[j], "es mayor que", lista[j + 1])
            print("Se deben intercambiar")
            
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
            print("PASO 10 - Lista después del intercambio:", lista)
        else:
            print("PASO 9 - No se intercambian")


print("PASO FINAL - Lista ordenada:", lista)