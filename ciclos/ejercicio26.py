cant=int(input("Ingrese la cantidad de números que desea ingresar: "))
negativos=0
cero=0
positivos=0
for i in range(cant):
    num=int(input("Digite un numero: "))
    if num<0:
        negativos+=1
    elif num==0:
        cero+=1
    else:
        positivos+=1
print(f"""\nPositivos: {positivos}
Negativos: {negativos}
Ceros: {cero}""")