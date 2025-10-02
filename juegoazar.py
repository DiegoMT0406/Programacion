import random

numeroAzar = random.randint(1, 100)
# Copiado de ChatGPT porque en los apuntes no lo encontraba

numeroAdivinado = int(input("Intenta adivinar un número entre 1 y 100: "))

while numeroAdivinado != numeroAzar:
	if numeroAdivinado < numeroAzar:
		print("Muy bajo. Inténtalo de nuevo.")
	if numeroAdivinado > numeroAzar:
		print("Muy alto. Inténtalo de nuevo.")
	numeroAdivinado = int (input("Intenta adivinar un número entre 1 y 100: "))

if numeroAdivinado == numeroAzar:
	print("Acertaste")
