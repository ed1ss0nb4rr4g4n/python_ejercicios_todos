numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Opciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

operacion = input("Seleccione una operación (1-4): ")

if operacion == "1":
    resultado = numero1 + numero2
elif operacion == "2":
    resultado = numero1 - numero2
elif operacion == "3":
    resultado = numero1 * numero2
elif operacion == "4":
    if numero2 == 0:
        print("No se puede dividir entre cero.")
    else:
        resultado = numero1 / numero2
else:
    print("Opción no válida.")

if operacion in ("1", "2", "3") or (operacion == "4" and numero2 != 0):
    print(f"El resultado es: {resultado}")