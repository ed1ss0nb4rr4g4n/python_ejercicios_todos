diccionario={}
lista1=[]
frase=str(input(f"Digite una frase: "))
lista1=frase.split()
contador=0

for palabra in lista1:
    if palabra not in diccionario:
        diccionario.update({palabra:contador})

for palabra in diccionario:
    contador=0
    for palabra2 in lista1:
        if palabra==palabra2:
            contador+=1
            diccionario.update({palabra:contador})

        
for palabra,contador in diccionario.items():
    print(f"{palabra}:{contador}")
