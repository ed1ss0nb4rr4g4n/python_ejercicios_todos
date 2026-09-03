#Desarrolle un programa que solicite el nombre de 
#un empleado, la cantidad de horas trabajadas y el 
#valor de la hora. El programa debe calcular el
#salario total e imprimir toda la información.

nombre=str(input("Digite el nombre de el empleado: "))
horasTrabajadas=int(input("Digite la cantidad de horas trabajadas: "))
valorHora=int(input("Digite el valor de la hora: "))

salarioTotal=valorHora*horasTrabajadas

print(f"-"*30)
print(f"Nombre: {nombre}")
print(f"Cantidad de horas trabajadas: {horasTrabajadas}")
print(f"Valor por hora: {valorHora}")
print(f"Salario total: {salarioTotal}")
