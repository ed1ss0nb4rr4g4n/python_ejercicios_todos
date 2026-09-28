Algoritmo controlDeAcceso
	Definir cantidadPersonas,i,edad como entero;
	definir nombre, boleta como cadena;
	definir S,N como caracter;
	Escribir 'Digite la cantidad de de personas que van a ingresar: ';
	leer cantidadPersonas;
	
	
	si cantidadPersonas>0 Entonces
		Para i<-1 Hasta CantidadPersonas Con Paso 1 Hacer
			escribir 'la persona ',i, ' tiene boleta?:';
			
			repetir 
				escribir 'Digite ¨S¨ para si.Digite ¨N¨ para no';
				leer boleta;
				boleta<-mayusculas(boleta);
			hasta que boleta="N" o boleta="S" 
			
			
			si boleta="N" entonces 
				escribir'No puede ingresar por que no tiene boleta';
				escribir'__________________________________________';
			FinSi
			
			si boleta="S" entonces	
				Escribir'Escriba el nombre de la persona ',i;
				leer nombre;
				escribir'Digite la edad de la persona ',i;
				leer edad;
				Si edad>0 y edad<5 entonces 
					escribir 'No puede ingresar';
					escribir'__________________________________________';
				SiNo
					Si edad<=11 y 5<=edad Entonces
						escribir'Debe ingresar con un adulto';
						escribir'__________________________________________';
					SiNo
						si edad>=12 Entonces
							escribir 'Puede ingresar';
							escribir'__________________________________________';
						FinSi
						
					FinSi
				FinSi
			FinSi
		FinPara
	FinSi
	si cantidadPersonas<=0 Entonces
		Escribir "No es un número valido!.";
	FinSi
FinAlgoritmo
