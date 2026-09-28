compra=int(input("Ingrese el monto de la compra: "))
descuento=0
if compra>500000:
    descuento=compra*0.10
    total=compra-descuento
    print(f"El descuento de la compra es de : {descuento}")
    print(f"Total a pagar: {total}")
else:
    print(f"El descuento de la compra es de : {descuento:.2f}")
    print(f"Total a pagar: {compra}")