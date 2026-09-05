def suma(a,b):
     return a+b
def resta(a,b):
     return a-b
def multiplicacion(a,b):
     return a*b
def division(a,b):
     return a/b



while True:
    print("""Menu de opciones:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir 
5. romper""")
    option=int(input("\nDigite la opcion a elegir del 1 al 5: "))
    a=int(input("Digite el primer valor: "))
    b=int(input("Digite el segundo valor: "))
    if option==1:
        sumas=suma(a,b)
        print("-"*50)
        print(f"\nEl resultado de las suma es: {sumas}")
        print("-"*50)
        print("")
    if option==2: 
        restas=resta(a,b)
        print("-"*50)
        print(f"\nEl resultado de la resta es: {restas}")
        print("-"*50)
        print("")
    if option==3:
        multiplicacions=multiplicacion(a,b)
        print("-"*50)
        print(f"\nEl resultado de la multiplicacion es: {multiplicacions}")
        print("-"*50)
        print("")
    if option==4:
        divisions=division(a,b)
        print("-"*50)
        print(f"\nEl resultado de la division es de {divisions}")
        print("-"*50)
        print("")
    if option==5:
            print("A salido")
            break
print("-"*50)
print(f"El resultado de la division es de {divisions}")
print("-"*50)
print("")