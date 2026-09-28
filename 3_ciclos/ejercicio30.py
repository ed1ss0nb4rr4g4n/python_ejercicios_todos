cant = int(input("¿Cuántos términos de Fibonacci desea generar? "))

a = 0
b = 1

print("Serie de Fibonacci:")

for i in range(cant):
    print(a, end=" ")
    
    x = a + b
    a = b
    b = x