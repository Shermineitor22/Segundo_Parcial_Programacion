from validaciones import pedir_entero


def mostrar_mayor_nota(alumnos: dict[int, dict]) -> None:
    """Muestra por consola la mayor nota final registrada entre los alumnos.

    Verifica si hay alumnos cargados; si el diccionario está vacío, informa que
    no hay registros. De lo contrario, recorre los valores de `alumnos` para
    encontrar la mayor `'nota_final'` y el nombre asociado, e imprime el
    resultado.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}, donde cada
            valor contiene las claves `'nombre'` y `'nota_final'`.

    Returns:
        None.
    """
    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados.")
        return None

    mayor_nota = -1.0
    nombre_mayor = ""

    for alumno in alumnos.values():
        if alumno["nota_final"] > mayor_nota:
            mayor_nota = alumno["nota_final"]
            nombre_mayor = alumno["nombre"]

    print(f"\nEl alumno con mayor nota es: nombre: {nombre_mayor}, nota final: {mayor_nota}")
    return None


def mostrar_alumnos(alumnos: dict[int, dict]) -> None:
    """Muestra por consola la cantidad total de alumnos registrados.

    Verifica si hay alumnos cargados; si el diccionario está vacío, informa que
    no hay registros. De lo contrario, imprime la cantidad de elementos
    presentes en `alumnos`.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        None.
    """
    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados.")
        return None

    print(f"\nCantidad de alumnos registrados: {len(alumnos)}")
    return None


def promedio_notas(alumnos: dict[int, dict]) -> None:
    """Calcula y muestra por consola el promedio de notas finales de los alumnos.

    Verifica si hay alumnos cargados; si el diccionario está vacío, informa que
    no hay registros. De lo contrario, suma el campo `'nota_final'` de cada
    alumno, divide por la cantidad total de registros e imprime el promedio
    formateado a dos decimales.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}, donde cada
            valor contiene la clave `'nota_final'`.

    Returns:
        None.
    """
    promedio_total = 0

    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados.")
        return None

    for alumno in alumnos.values():
        promedio_total += alumno["nota_final"]

    promedio = promedio_total / len(alumnos)
    print(f"\nPromedio de notas: {promedio:.2f}")
    return None


def mostrar_aprobados(alumnos: dict[int, dict]) -> None:
    """Muestra por consola la cantidad de alumnos aprobados.

    Verifica si hay alumnos cargados; si el diccionario está vacío, informa que
    no hay registros. De lo contrario, cuenta los alumnos con nota final mayor o
    igual a 6 e imprime la cantidad.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        None.
    """
    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados.")
        return None

    cantidad_aprobados = 0
    for alumno in alumnos.values():
        if alumno["nota_final"] >= 6:
            cantidad_aprobados += 1
    print(f"\nCantidad de alumnos aprobados: {cantidad_aprobados}")
    return None


def mostrar_desaprobados(alumnos: dict[int, dict]) -> None:
    """Muestra por consola la cantidad de alumnos desaprobados.

    Verifica si hay alumnos cargados; si el diccionario está vacío, informa que
    no hay registros. De lo contrario, cuenta los alumnos con nota final menor a
    6 e imprime la cantidad.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}, donde cada
            valor contiene la clave `'nota_final'`.

    Returns:
        None.
    """
    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados.")
        return None

    cantidad_desaprobados = 0
    for alumno in alumnos.values():
        if alumno["nota_final"] < 6:
            cantidad_desaprobados += 1
    print(f"\nCantidad de alumnos desaprobados: {cantidad_desaprobados}")
    return None


def ver_estadisticas(alumnos: dict[int, dict]) -> None:
    """Muestra un menú interactivo para consultar las estadísticas de los alumnos.

    Verifica si hay alumnos cargados; si el diccionario está vacío, informa que
    no hay datos para calcular estadísticas y retorna `None`. De lo contrario,
    muestra las opciones disponibles y ejecuta la función correspondiente según
    la elección del usuario hasta seleccionar volver al menú principal.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        None.
    """
    salir = False

    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados para calcular estadísticas.")
        return None

    print("\nEstadísticas de los alumnos:")
    print("\n1. Cantidad de alumnos registrados")
    print("2. Promedio de notas")
    print("3. Alumno con mayor nota final")
    print("4. Cantidad de alumnos aprobados")
    print("5. Cantidad de alumnos desaprobados")
    print("6. Volver al menú principal")

    while not salir:
        opcion = pedir_entero("\nSeleccione una opción: ")

        match opcion:
            case 1:
                mostrar_alumnos(alumnos)
            case 2:
                promedio_notas(alumnos)
            case 3:
                mostrar_mayor_nota(alumnos)
            case 4:
                mostrar_aprobados(alumnos)
            case 5:
                mostrar_desaprobados(alumnos)
            case 6:
                print("Volviendo al menú principal...")
                salir = True
            case _:
                print("Opción no válida, intente de nuevo.")

    return None