print("Digite la longitud de los lados de tres lados para determinar si equilatero, isoceles o escaleno")
l1=int(input("Digite la longitud del lado 1: "))
l2=int(input("Digite la longitud del lado 2: "))
l3=int(input("Digite la longitud del lado 3: "))

if l1==l2==l3:
    print("Es equilatero")
elif l1==l2 or l1==l3 or l2==l3:
    print("Es isoceles")
else:
    print("Es escaleno")