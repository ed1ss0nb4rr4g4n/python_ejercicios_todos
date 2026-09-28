Algoritmo suma_resta_multiplicacion_division
	Definir num1, num2 Como Entero
	Definir sum,rest,multi,divi como real
	Escribir 'Digite el primer numero'
	leer num1
	Escribir 'digite el segundo numero'	
	leer num2
	sum<-num1+num2
	rest<-num1-num2
	multi<-num1*num2
	
	Escribir 'Suma -> ',sum
	Escribir 'Resta -> ',rest
	Escribir 'Multiplicacion-> ',multi
	Si num2<0 Entonces
		Escribir 'No se puede dividir'
	SiNo
		divi<-num1/num2
		Escribir 'la Division es ',divi
	Fin Si
FinAlgoritmo