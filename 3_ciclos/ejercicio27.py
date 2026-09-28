num=int(input("Digite un número entero positivo: "))
suma=0
for i in range(1,num+1):
    if i%2!=0:
        suma+=i
print(f"\nLa suma de los números impares es: {suma}")