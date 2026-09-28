Proceso ejemplo_listas_o_arreglos
	definir i como entero;
	definir students como cadena;
	definir value,promedio como real;
	Definir suma Como Numerico;
	
	dimensionar students[5];
	dimensionar value[5];
	
	para i<-0 hasta 4 hacer 
		escribir 'Ingrese el nombre del estudiante ',i+1,':';
		Leer students[i];
	
		escribir 'Ingrese la nota del estudiante ',i+1,':';
		Leer value[i];
		Si value[i]>=3.5 entonces
			escribir '___________________________________________';
			escribir'El alumno a aprobado';
			escribir '___________________________________________';
		SiNo
			escribir '___________________________________________';
			Escribir'El alumno a reprobado';
			escribir '___________________________________________';
		FinSi
	FinPara
	
	
	suma<-0;
	Para i<-0 Hasta 4 Hacer 
		suma<-suma+value[i];
	FinPara
	promedio<-suma/5;
	
	//escribir ciclo para escribir
	para i<-0 hasta 4 hacer 
		escribir i+1,'.',students[1],' obtuvo ',value[i];
	finpara
	
	escribir'El promedio de las nostas en general de los etudiantes es de: ',promedio;
FinProceso
