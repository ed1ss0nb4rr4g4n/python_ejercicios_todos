num=int(input("Digite un número entero positivo para calcular su factorial "))
num1=num
for i in range(num,1, -1):
    num*=i-1
print(f"\n El factorial de {num1} es {num}")