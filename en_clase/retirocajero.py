saldo=2000000
ctrTru="Contraseña123"
contador=0
def menu():
    print("""CAJERO AUTOMATICO
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir""")
print(f"Bienvenido")

while True:
    ctr=str(input(f"Digite la contraseña:\n"))
    if ctr!=ctrTru:
        contador+=1
        if contador< 3:
            print("Contraseña incorrecta, intente otra vez:C ")
        elif contador==3:
            print(f"Intentelo de nuevo mas tarde")
            break
    elif ctr==ctrTru:
        while True:
            menu()
            op=int(input(f"\nIngrese la opcion a elegir:\n"))
            match op:
                case 1:
                    print(f"Su saldo es de {saldo}")
                case 2:
                    deposita=int(input("Digite el valor a depositar: "))
                    saldo+=deposita
                    print(f"A depositado: {deposita} su saldo es de: {saldo}")
                case 3:
                    retiro=int(input("Digite el valor a retirar: "))
                    saldo-=retiro
                    print(f"A retirado: {retiro}, su saldo actual es de: {saldo}")
                case 4:
                    break
        
                
                