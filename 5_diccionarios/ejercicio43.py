productos={}
cant=int(input(f"Digite la cantidad de productos: "))
for i in range(cant):
    productos.update({str(input(f"Digite el producto {i+1}: ")): int(input(f"Digite la cantidad del producto: "))})
buscar=str(input(f"\nDigite el producto que desa buscar: "))
print(f"Cantidad disponible de {buscar.title()} -> {productos.get(buscar)}")