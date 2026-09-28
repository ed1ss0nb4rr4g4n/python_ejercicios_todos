abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

resultado = []
contador = 0

for letra in abecedario:
    contador += 1
    if contador == 3:
        contador = 0 
    else:
        resultado.append(letra) 

print(resultado)