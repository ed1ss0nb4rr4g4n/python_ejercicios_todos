# 1. Pedir la palabra al usuario y convertirla a minúsculas
palabra = input("Ingrese una palabra: ").lower()

# 2. Recorrer cada vocal y contar sus apariciones
for vocal in "aeiou":
    cantidad = palabra.count(vocal)
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")