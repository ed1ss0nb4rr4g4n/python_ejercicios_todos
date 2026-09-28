diccionario_contador = {}
lista_filtrada = []
frase = str(input("Indique la palabra: "))
lista_letras = list(frase)

for i in lista_letras:
    if i not in lista_filtrada:
        lista_filtrada.append(i)

for i in lista_filtrada:
    contador=0
    for j in lista_letras:
        if i==j:
            contador+=1
    diccionario_contador.update({i:contador})

for palabra, count in diccionario_contador.items():
    print(f"{palabra}:{count}")