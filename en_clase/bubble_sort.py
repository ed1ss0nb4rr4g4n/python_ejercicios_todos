lista1=[7,3,1,2,4,6,9,5,8]

for i in lista1:
    for j in range(len(lista1-1)):
        if lista1[j] > lista1[j+1]:
            lista1[j], lista1[j+1] = lista1[j+1], lista1[j]
print(*lista1)