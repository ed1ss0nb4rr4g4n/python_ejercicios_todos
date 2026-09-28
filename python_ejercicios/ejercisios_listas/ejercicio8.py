palabra = input("Ingrese una palabra: ")

palabra_limpia = ""
for caracter in palabra.lower():
    if caracter != " ":
        palabra_limpia += caracter
print(palabra_limpia)

palabra_invertida = ""
for letra in palabra_limpia:
    palabra_invertida = letra + palabra_invertida
print(palabra_invertida)


if palabra_limpia == palabra_invertida:
    print(f"La palabra '{palabra}' SÍ es un palíndromo.")
else:
    print(f"La palabra '{palabra}' NO es un palíndromo.")