agenda={}
cant=int(input(f"Ingrese la cantidad de contactos a agregar: "))
for i in range(cant):
    agenda.update({str(input(f"Digite el nombre de la persona: ")): int(input(f"Digite el contacto de la persona: "))})

buscar=str(input(f"Digite el contacto que desea buscar"))

print(buscar,agenda.get(buscar))

