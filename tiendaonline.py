articulos = []
menuInventarioArticulos = ("1. Crear artículo", "2. Listar artículos", "3. Buscar artículo por id", "4. Actualizar artículo", "5. Eliminar artículo", "6. Alternar activo/inactivo", "7. Salir")
accionesMenuInventarioArticulos = 0
# Definimos listas y variables

def leer_float(texto, minimo=0.01): #Esta función y la que hay debajo funcionan de forma casi idéntica: reciben un valor y comparan si está por encima del mínimo o si es válido. Si es así, lo devuelven igual. Si no, lo vuelven a pedir.
    while True:
        try:
            valor = float(input(texto))
            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Ese número no vale. Introduce otro.")

def leer_int(texto, minimo=0): 
    while True:
        try:
            valor = int(input(texto))
            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Ese número no vale. Introduce otro.")

def generar_id(articulos): # Para generar un ID mira si la lista está vacía. Si lo está, da un 1. Si no lo está, busca el máximo número y le suma 1.
    if len(articulos) == 0:
        return 1
    else:
        return max(articulo["id"] for articulo in articulos) + 1

def crear_articulo(articulos): # En esta función te pide que introduzcas el nombre. Después, se vale de las dos funciones que creamos antes para validar que el stock y el precio son cosas coherentes y después añade estos valores a un diccionario que se guardará en nuestra lista de artículos. Mientras hace eso, también genera un ID único.
    nombre = input("Nombre: ")
    precio = leer_float("Precio: ", minimo=0.01)
    stock = leer_int("Stock: ", minimo=0)
    articulo = {"id": generar_id(articulos), "nombre": nombre, "precio": precio, "stock": stock, "activo": True}
    articulos.append(articulo)
    print("El artículo se ha añadido a la lista.")
    print("")

def listar_articulo(articulos): #Esta función imprime todos los artículos uno por uno, a menos que no haya ninguno.
    if len(articulos) == 0:
        print("No hay artículos en la lista")
        return
    else:
        for articulo in articulos:
            print(articulo)

def buscar_articulo_por_id(articulos, id_busqueda): #Esta función recorre todos los artículos uno por uno, y si el ID que buscamos coincide con alguno existente, lo devuelve.
    for articulo in articulos:
        if articulo["id"] == id_busqueda:
            print(f"Artículo con ID {articulo['id']}:")
            print(articulo)
            return articulo
    print("No se ha encontrado ningún artículo con ese ID.")
    return None

def actualizar_articulo(articulos): #Esta función se vale de la función de buscar artículo por ID que hicimos antes, y una vez tiene el artículo, te lo muestra y te permite cambiar su nombre, stock y precio. Si todo sale bien, te muestra los cambios realizados.
    id_busqueda = leer_int("Teclea el ID del artículo que quieras actualizar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        return
    print("Esas son las estadísticas actuales del artículo.")
    print("")
    articulo["nombre"] = input("Introduce el nuevo nombre del artículo: ")
    articulo["precio"] = leer_float("Introduce el nuevo precio del objeto: ")
    articulo["stock"] = leer_int("Introduce el nuevo stock del artículo: ")
    print("")
    print("Todo se ha modificado correctamente.")
    print("Estadísticas actuales del artículo:")
    print(articulo)

def borrar_articulo(articulos): #Esta función se vale de la función de buscar artículo por ID que hicimos antes, y una vez tiene el artículo, te lo muestra y te permite confirmar o cancelar la eliminación, escribiendo un 1 o un 0.
    id_busqueda = leer_int("Teclea el ID del artículo que quieras borrar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        return
    print("Has seleccionado este artículo.")
    borrarArticulo = int(input("¿Seguro que quieres borrarlo? (1 para decir sí, 0 para decir no): "))
    print("")
    match borrarArticulo:
        case 1:
            articulos.remove(articulo)
            print("Artículo borrado correctamente")
        case 0:
            print("Eliminación de artículo cancelada")
        case _:
            print("Solo se puede introducir 1 o 0.")

def alternar_activo(articulos): #Esta función se vale de la función de buscar artículo por ID que hicimos antes, y una vez tiene el artículo, invierte el estado de actividad en el que se encuentra. Si estaba activo, ahora no lo estará o viceversa.
    id_busqueda = leer_int("Teclea el ID del artículo que quieras desactivar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        return
    if articulo["activo"] == True:
        articulo["activo"] = False
        print(f"{articulo['nombre']} ya no está disponible.")
    else:
        articulo["activo"] = True
        print(f"{articulo['nombre']} ahora está disponible.")


while accionesMenuInventarioArticulos != 7: #Un match case con las distintas opciones del menú
    for menuinventarioarticulo in menuInventarioArticulos:
        print(menuinventarioarticulo)
    print("")
    accionesMenuInventarioArticulos = int(input("Teclea un número para realizar una acción: "))

    match accionesMenuInventarioArticulos:
        case 1:
            crear_articulo(articulos)

        case 2:
            print("Lista de artículos:")
            print("")
            listar_articulo(articulos)
            print("")

        case 3:
            print("")
            id_busqueda = leer_int("Introduce el ID del artículo que quieres buscar: ")
            buscar_articulo_por_id(articulos, id_busqueda)
            print("")

        case 4:
            print("")
            actualizar_articulo(articulos)
            print("")

        case 5:
            print("")
            borrar_articulo(articulos)
            print("")

        case 6:
            print("")
            alternar_activo(articulos)
            print("")

        case 7:
            print("")
            print("Gracias por usar el programa")

        case _:
            print("")
            print("Ese número no es válido. Introduce otro.")
            print("")
