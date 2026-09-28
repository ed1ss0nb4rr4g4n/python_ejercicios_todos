Proceso calculo_de_salario
Definir horasTrabajadas,valorHora,salarioBruto,salarioNeto,salario como Real;
Escribir 'Digite el valor de horas trabajadas en el mes';
Leer horasTrabajadas;
Escribir 'Digite el valor de la hora';
Leer valorHora;
salarioBruto<-valorHora*horasTrabajadas;
salarioNeto<-0.12*salarioBruto;
salario<-salarioBruto-salarioNeto;
Escribir '_______________________________________________';
Escribir 'El salario del trabajador con un descuento ';
Escribir 'del 12% por retencion de impuestos es de: ', salario;
Escribir '_______________________________________________';
FinProceso
