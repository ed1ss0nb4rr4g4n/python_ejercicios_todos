propietario = input("Nombre del propietario: ")
mascota = input("Nombre de la mascota: ")
especie = input("Especie de la mascota: ")

valor_consulta = float(input("Valor de la consulta: $"))

vacuna = float(input("Valor de las vacunas (0 si no aplica): $"))
medicamentos = float(input("Valor de los medicamentos (0 si no aplica): $"))
otros = float(input("Valor de otros servicios (0 si no aplica): $"))

subtotal = valor_consulta + vacuna + medicamentos + otros
iva = subtotal * 0.19
total = subtotal + iva

print("\n====================================")
print("      CLÍNICA VETERINARIA")
print("====================================")
print("Propietario:", propietario)
print("Mascota:", mascota)
print("Especie:", especie)

print("\nDetalle de la atención")
print("------------------------------")
print("Consulta:      $", valor_consulta)
print("Vacunas:       $", vacuna)
print("Medicamentos:  $", medicamentos)
print("Otros:         $", otros)

print("------------------------------")
print("Subtotal:      $", subtotal)
print("IVA (19%):     $", iva)
print("TOTAL A PAGAR: $", total)
print("====================================")