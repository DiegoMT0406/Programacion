
nIntroducido = int (input("Introduce tu número" ))

a = 0
pares = 0
if nIntroducido > 0:
	for numero in range (nIntroducido):
		a = a + 1
		comprobacion = a % 2
		if comprobacion == 0:
			pares = pares + 1
	print (numero + 1, "tiene", pares, "pares")
else: print ("El número debe ser superior a cero")
	
