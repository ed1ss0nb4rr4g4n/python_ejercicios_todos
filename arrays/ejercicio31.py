
cant=int(input("Digite la cantidad de numeros que desea ingresar: "))
nums=[]

for i in range(cant):
    nums.append(int(input("Digite un numero: ")))
for i in range(len(nums)):
    minimo=min(nums)
    maximo=max(nums)
print(f"""\nMayor: {maximo} 
Menor: {minimo}""")