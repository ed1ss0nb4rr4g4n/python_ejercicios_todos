# Forma 1
numeros=[]
print("Ingrese los numeros del 1 al 10: ")
for i in range (10):
    numeros.append(int(input(f"Ingrese el numero {i+1}: ")))
numeros.reverse()
print(numeros) 
print("-"*30)
# Forma 2
numeros = []
n = 10
print("Ingrese los numeros del 1 al 10: ")
for i in range(n):
    numeros.append(int(input(f"Ingrese el numero {i+1}: ")))

for i in range(n // 2):
    numeros[i], numeros[n - 1 - i] = numeros[n - 1 - i], numeros[i]

print(numeros)
