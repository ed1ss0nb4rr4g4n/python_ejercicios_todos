usuarioej="admin"
contraseñaej="Python123"

usuario=str(input("Digite su nombre de usuario: "))
clave=str(input("Digite su clave: "))

while True:
    if usuario==usuarioej and clave==contraseñaej:
        print("Bienvenido al sistema")
        break
    else:
        print("Usuario o clave incorrectos")
        usuario=str(input("Digite su nombre de usuario: "))
        clave=str(input("Digite su clave: "))