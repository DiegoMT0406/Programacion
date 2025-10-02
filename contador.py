n = int (input("Introduce tu número" ))

if n > 0:
	m = 0
	suma = 0
	while m < n:
		m = m + 1
		print ("ahora sumamos el", m)
		suma = suma + m
		print("La suma total es:", suma)
else: print ("Tu número no es positivo")
