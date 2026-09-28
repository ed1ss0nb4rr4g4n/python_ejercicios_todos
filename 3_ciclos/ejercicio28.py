palabra=str(input("ingrese una palabra o frase: "))
contador=0
for i in palabra:
    if i in "aeiou":
        contador+=1
print(f"\nLa palabra contiene {contador} vocales")