Proceso consumo_de_combustible
	definir distancia,galon,rendimiento,costo,galones como real;
	Escribir 'Digite la distacnia en km';
	leer distancia;
	Escribir 'Digite el precio del galon de combustible';
	leer galon;
	Escribir 'Digite cuantos km rinde el coche por galon';
	Leer rendimiento;
	galones<-distancia/rendimiento;
	costo<-galon*galones;
	Escribir 'El costo total es de: ',costo;
 
FinProceso
