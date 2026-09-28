numero=int(input("Digite un numero de dos digitos a continuacion: "))
decenas=int(numero/10)
unidades=int(numero-decenas*10)
print("El numero",numero,"tiene",decenas,"descenas y tiene",unidades,"unidades.")

#Segunda forma
numero=int(input("Digite un numero de dos digitos a continuacion: "))
decenas=numero // 10
unidades=numero % 10
print("El numero",numero,"tiene",decenas,"descenas y tiene",unidades,"unidades.")