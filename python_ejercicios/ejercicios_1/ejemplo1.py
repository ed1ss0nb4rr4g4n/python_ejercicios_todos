nombreCliente=input("Digite el nombre del cilente ")
procesador=input("Digite el procesador del cliente ")
ram=input("Digite la RAM del computador ")
disco=input("Digite el disco del computador ")
procesadorValor=float(input("Digite el precio del procesador "))
ramValor=float(input("Digite el precio de la ram "))
discoValor=float(input("Digite eñ precio del disco "))

sumaComponentes=discoValor+ramValor+procesadorValor
iva=sumaComponentes/0.19
valorTotalIva=iva+sumaComponentes
print("_________________________")
print("Resumen de la Compra")
print("_________________________")
print("El cliente", nombreCliente, " a comprado los siguientes componentes:")
print("Un procesador ",procesador,". Valor: ",procesadorValor)
print("Una ram ",ram,". Valor: ",ramValor)
print("Un disco ",disco,". Valor: ",discoValor)
print("_________________________")
print("El valor total es de ",sumaComponentes)
print("El iva es: ",iva)
print("El valor total de los componentes con IVA es ",valorTotalIva)
print("_________________________")
print("Gracias por su compra")
