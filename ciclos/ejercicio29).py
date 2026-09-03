numero = int(input("Número: "))

es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")