accionesInicio = 0
accionesMenuInventarioArticulos = 0
menuInicio =("1. Inventario de artículos", "2. Gestión de usuarios", "3. Carrito y ventas", "4. Salir")
detenerMenuInicio = False
articulos = []
menuInventarioArticulos = ("1. Crear artículo", "2. Listar artículos", "3. Buscar artículo por id", "4. Actualizar artículo", "5. Eliminar artículo", "6. Alternar activo/inactivo", "7. Volver al menú principal")
accionesMenuInventarioArticulos = 0
usuarios = []
menuUsuarios =("1. Crear usuario","2. Listar usuarios", "3. Buscar usuario por id", "4. Actualizar usuario", "5. Eliminar usuario", "6. Alternar activo/inactivo", "7. Volver al menú principal")
accionesMenuUsuarios = 0
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


#Estas son las funciones de uso general




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


#Estas son las funciones del menú Artículos


def crear_usuario(usuarios):  # Esta función pide el nombre y el email del usuario, valida que el email tenga "@" y ".", genera un ID único y añade el usuario a la lista.
    nombre = input("Nombre del usuario: ")
    emailValido = False
    while not emailValido:
        email = input("Email del usuario: ")
        if "@" in email and "." in email:
            emailValido = True
        else:
            print("El email no es válido. Debe contener '@' y '.'")

    usuario = {"id": generar_id(usuarios), "nombre": nombre, "email": email, "activo": True}
    usuarios.append(usuario)
    print("Usuario creado correctamente")
    print("")


def listar_usuario(usuarios): #Esta función imprime todos los usuarios uno por uno, a menos que no haya ninguno.
    if len(usuarios) == 0:
        print("No hay usuarios en la lista")
        return
    else:
        for usuario in usuarios:
            print(usuario)


def buscar_usuario_por_id(usuarios, id_busqueda): #Esta función recorre todos los usuarios uno por uno, y si el ID que buscamos coincide con alguno existente, lo devuelve.
    for usuario in usuarios:
        if usuario["id"] == id_busqueda:
            print(f"Usuario con ID {usuario['id']}:")
            print(usuario)
            return usuario
    print("No se ha encontrado ningún usuario con ese ID.")
    return None


def actualizar_usuario(usuarios): #Esta función se vale de la función de buscar usuario por ID que hicimos antes, y una vez tiene el usuario, te lo muestra y te permite cambiar su nombre y su email, revisando que tenga un "@" y un ".". Si todo sale bien, te muestra los cambios realizados.
    id_busqueda = leer_int("Teclea el ID del artículo que quieras actualizar: ")
    usuario = buscar_usuario_por_id(usuarios, id_busqueda)
    if not usuario:
        return
    print("Estos son los datos actuales del usuario:")
    print("")
    usuario["nombre"] = input("Introduce el nuevo nombre del usuario: ")
    emailValido = False
    while not emailValido:
        usuario["email"] = input("Introduce el nuevo email del usuario: ")
        if "@" in usuario["email"] and "." in usuario["email"]:
            emailValido = True
        else:
            print("El email no es válido. Debe contener '@' y '.'")
    print("")
    print("Todo se ha modificado correctamente.")
    print("Datos actuales del usuario:")
    print(usuario)


def borrar_usuario(usuarios): #Esta función se vale de la función de buscar usuario por ID que hicimos antes, y una vez tiene el usuario, te lo muestra y te permite confirmar o cancelar la eliminación, escribiendo un 1 o un 0.
    id_busqueda = leer_int("Teclea el ID del usuario que quieras borrar: ")
    usuario = buscar_usuario_por_id(usuarios, id_busqueda)
    if not usuario:
        return
    print("Has seleccionado este usuario.")
    borrarUsuario = int(input("¿Seguro que quieres borrarlo? (1 para decir sí, 0 para decir no): "))
    print("")
    match borrarUsuario:
        case 1:
            usuarios.remove(usuario)
            print("Usuario borrado correctamente")
        case 0:
            print("Eliminación de usuario cancelada")
        case _:
            print("Solo se puede introducir 1 o 0.")


def alternar_activo(usuarios): #Esta función se vale de la función de buscar usuario por ID que hicimos antes, y una vez tiene el usuario, invierte el estado de actividad en el que se encuentra. Si estaba activo, ahora no lo estará o viceversa.
    id_busqueda = leer_int("Teclea el ID del artículo que quieras desactivar: ")
    usuario = buscar_usuario_por_id(usuarios, id_busqueda)
    if not usuario:
        return
    if usuario["activo"] == True:
        usuario["activo"] = False
        print(f"{usuario['nombre']} ya no está disponible.")
    else:
        usuario["activo"] = True
        print(f"{usuario['nombre']} ahora está disponible.")



while accionesInicio != 4 and detenerMenuInicio == False: 
    for menus in menuInicio:
        print(menus)
    print("")
    accionesInicio = int(input("Teclea un número para acceder a un menú: "))

    match accionesInicio:
        case 1:  # Cuando llegas al primer menú, se deja de repetir
            detenerMenuInicio = True
            while accionesMenuInventarioArticulos != 7:  # Un match case con las distintas opciones del menú
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
                        detenerMenuInicio = False

                    case _:
                        print("")
                        print("Ese número no es válido. Introduce otro.")
                        print("")



        case 2: 
            detenerMenuInicio = True
            while accionesMenuUsuarios != 7:  # Un match case con las distintas opciones del menú
                for menuUsuario in menuUsuarios:
                    print(menuUsuario)
                print("")

                accionesMenuUsuarios = int(input("Teclea un número para realizar una acción: "))

                match accionesMenuUsuarios:
                    case 1:
                        crear_usuario(usuarios)

                    case 2:
                        print("Lista de usuarios:")
                        print("")
                        listar_usuario(usuarios)
                        print("")

                    case 3:
                        print("")
                        id_busqueda = leer_int("Introduce el ID del usuario que quieras buscar: ")
                        buscar_usuario_por_id(usuarios, id_busqueda)
                        print("")

                    case 4:
                        print("")
                        actualizar_usuario(usuarios)
                        print("")

                    case 5:
                        print("")
                        borrar_usuario(usuarios)
                        print("")

                    case 6:
                        print("")
                        alternar_activo(usuarios)
                        print("")

                    case 7:
                        detenerMenuInicio = False

                    case _:
                        print("")
                        print("Ese número no es válido. Introduce otro.")
                        print("")





































        case 3:
            detenerMenuInicio = True
            print ("Aquí irá el menú de carrito y ventas")
        case 4:
            detenerMenuInicio = True
            print ("")
            print ("Gracias por usar nuestros servicios")
        case _:
            print ("")
            print ("Ese no es un número válido")
