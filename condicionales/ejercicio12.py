numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

mayor = numero1

if numero2 > mayor:
    mayor = numero2
if numero3 > mayor:
    mayor = numero3

print(f"El número mayor es: {mayor}")