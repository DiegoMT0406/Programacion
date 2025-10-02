palabra = input("Introduce tu palabra")

vocalesEnPalabra = 0
vocales = "aeiouAEIOU"
for vocal in palabra:
    if vocal in vocales:
        vocalesEnPalabra = vocalesEnPalabra + 1
print("La cantidad de vocales en tu palabra es", vocalesEnPalabra)
