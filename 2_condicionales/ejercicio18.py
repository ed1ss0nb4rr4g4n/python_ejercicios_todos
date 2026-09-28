print("Digite la longitud de los lados de tres lados para determinar si es posible formar un triangulo")
l1=int(input("Digite la longitud del lado 1: "))
l2=int(input("Digite la longitud del lado 2: "))
l3=int(input("Digite la longitud del lado 3: "))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print("Si es posible formar un triangulo")
else:
    print("No es posible formar un triangulo")