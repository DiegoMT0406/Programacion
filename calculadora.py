n1 = int (input("Cuál es el primer número?" ))
n2 = int (input("Cuál es el segundo número?" ))


operacion = str (input("Qué operación quieres efectuar?" ))

if operacion == "suma":
	resultado = n1 + n2
	print (resultado)
if operacion == "resta": 
	resultado = n1 - n2
	print (resultado)
if operacion == "multiplicacion":
	resultado = n1 * n2
	print (resultado)
if operacion == "division":
	if n2 == 0:
		print ("Tu segundo número no puede ser cero")
	else:
		resultado = n1 / n2
		print (resultado)
