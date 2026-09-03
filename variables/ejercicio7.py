#Solicite el precio de un producto y el porcentaje de descuento aplicado. Calcule el valor del descuento y el precio final a pagar.

#Ejemplo de entrada

##Precio: 850000
##Descuento: 15

precioProducto=float(input("Ingrese el precio del producto: "))
descuento=float(input("Digite el porcentaje de descuento aplicado: "))

valorDescuento=(precioProducto*descuento)/100
precioFinal=precioProducto-valorDescuento

print(f"Precio del producto: {precioProducto}")
print(f"Valor del descuento: {valorDescuento}")
print(f"Precio final a pagar: {precioFinal}")