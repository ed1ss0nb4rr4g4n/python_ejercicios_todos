saldo=2000000
userTru="usuario"
ctrTru="Contraseña123"

def menu():
    print("""CAJERO AUTOMATICO
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir""")

while True:
    menu()
    user=str(input(f"Digite el usuario:\n"))
    ctr=str(input(f"Digite la contraseña:\n"))
    if ctr==ctrTru
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
    else:
        print(f"Usuario o contraseña incorrecta, intentalo nuevamente")
        
         