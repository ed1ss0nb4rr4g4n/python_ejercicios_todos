list=[]
n=5
print(f"Introduce los números ganadores de la lotería primitiva:")
for i in range(n):
    list.append(int(input(f"Introduce el numero {i+1}: ")))
for i in range (n):
    for j in range (0,n-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)