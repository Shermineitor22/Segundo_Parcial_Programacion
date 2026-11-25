from validaciones import (
    pedir_dni,
    pedir_edad,
    pedir_entero,
    pedir_nota,
    pedir_texto,
)
from archivos import guardar_alumnos


def alumnos_vacios(alumnos: dict[int, dict]) -> bool:
    """Verifica si el diccionario de alumnos está vacío.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        True si `alumnos` está vacío, False en caso contrario.
    """
    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados.")
        return True
    return False



def buscar_dni(alumnos: dict[int, dict], dni: int) -> int | None:
    """Busca un DNI dentro del diccionario de alumnos.

    Recorre las claves del diccionario y devuelve el DNI si existe. Si no se
    encuentra ninguna coincidencia, devuelve None.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.
        dni: Número de DNI a buscar.

    Returns:
        El DNI encontrado como entero si existe en `alumnos`, o None en caso contrario.
    """
    for clave in alumnos:
        if clave == dni:
            return clave
    return None


def registrar_alumnos(alumnos: dict[int, dict]) -> dict[int, dict]:
    """Registra uno o más alumnos solicitando y validando sus datos por consola.

    Pide la cantidad de alumnos a cargar y, por cada uno, solicita DNI, nombre,
    apellido, edad y nota final, evitando DNIs duplicados dentro del registro.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        Un diccionario con el formato {dni: datos_alumno}, donde cada valor
        contiene las claves 'nombre', 'apellido', 'edad' y 'nota_final'.
    """
    cantidad = pedir_entero("\nIngrese la cantidad de alumnos a registrar: ")

    for i in range(cantidad):
        print(f"\nRegistro del alumno {i + 1}")

        dni = pedir_dni("\nIngrese el DNI del alumno: ")
        while buscar_dni(alumnos, dni) is not None:             
            print("Error: el DNI ingresado ya existe. Ingrese otro.")
            dni = pedir_dni("\nIngrese el DNI del alumno: ")

        nombre = pedir_texto("\nIngrese el nombre del alumno: ")
        apellido = pedir_texto("\nIngrese el apellido del alumno: ")
        edad = pedir_edad("\nIngrese la edad del alumno: ")
        nota_final = pedir_nota("\nIngrese la nota final del alumno: ")

        alumnos[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "nota_final": nota_final,
        }
        print("\nAlumno registrado exitosamente.")

    print("Registro de alumnos completado.")
    print(f"Alumnos registrados: {cantidad}")
    guardar_alumnos(alumnos)
    return alumnos


def buscar_alumno(alumnos: dict[int, dict]) -> None:
    """Busca un alumno por DNI y muestra sus datos por consola si existe.

    Verifica si hay alumnos registrados, solicita y valida un DNI y lo busca
    en el diccionario de alumnos. Si lo encuentra, imprime sus datos; en caso
    contrario, informa que no se encontró y retorna `None`.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        None.
    """
    if alumnos_vacios(alumnos):
        return None

    dni = pedir_dni("\nIngrese el DNI del alumno a buscar: ")
    alumno_encontrado = buscar_dni(alumnos, dni)

    if alumno_encontrado is not None:
        alumno = alumnos[alumno_encontrado]
        print(f"\nDNI: {alumno_encontrado}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Nota final: {alumno['nota_final']}")
        return None

    print("Alumno no encontrado.")
    return None


def modificar_alumno(alumnos: dict[int, dict]) -> dict[int, dict]:
    """Modifica los datos de un alumno existente buscado por su DNI.

    Verifica si hay alumnos registrados, solicita un DNI válido y lo busca en
    `alumnos`. Si lo encuentra, muestra sus datos actuales, pide los nuevos
    valores validados (nombre, apellido, edad y nota final), actualiza el
    registro y devuelve el diccionario `alumnos`.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        El diccionario `alumnos` con el formato {dni: datos_alumno}.
    """
    if alumnos_vacios(alumnos):
        return alumnos

    dni = pedir_dni("\nIngrese el DNI del alumno a modificar: ")
    alumno_encontrado = buscar_dni(alumnos, dni)

    if alumno_encontrado is not None:
        alumno = alumnos[alumno_encontrado]
        print("\nAlumno encontrado:")
        print(f"\nDNI: {alumno_encontrado}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Nota final: {alumno['nota_final']}")

        nombre = pedir_texto("\nIngrese el nuevo nombre del alumno: ")
        apellido = pedir_texto("\nIngrese el nuevo apellido del alumno: ")
        edad = pedir_edad("\nIngrese la nueva edad del alumno: ")
        nota_final = pedir_nota("\nIngrese la nueva nota final del alumno: ")

        alumnos[alumno_encontrado] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "nota_final": nota_final,
        }

        print("\nAlumno modificado exitosamente.")
    else:
        print("\nAlumno no encontrado.")
    guardar_alumnos(alumnos)
    return alumnos


def eliminar_alumno(alumnos: dict[int, dict]) -> dict[int, dict]:
    """Elimina un alumno del diccionario a partir de su DNI y devuelve el diccionario.

    Verifica si hay alumnos registrados, solicita un DNI válido y lo busca en
    `alumnos`. Si lo encuentra, elimina la clave del diccionario y devuelve
    `alumnos` actualizado; si no hay alumnos o no se encuentra el DNI, devuelve
    `alumnos` sin cambios.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        El diccionario `alumnos` con el formato {dni: datos_alumno}.
    """
    if alumnos_vacios(alumnos):
        return alumnos

    dni = pedir_dni("\nIngrese el DNI del alumno a eliminar: ")
    alumno_encontrado = buscar_dni(alumnos, dni)

    if alumno_encontrado is not None:
        del alumnos[alumno_encontrado]
        print("\nAlumno eliminado exitosamente.")
    else:
        print("\nAlumno no encontrado.")

    guardar_alumnos(alumnos)
    return alumnos


def listar_alumnos(alumnos: dict[int, dict]) -> bool:
    """Muestra por consola todos los alumnos registrados e indica si hubo registros.

    Verifica si hay alumnos cargados; si el diccionario está vacío, informa que
    no hay registros y retorna `False`. De lo contrario, recorre cada par
    clave-valor, imprime el DNI y los datos asociados de cada alumno y
    retorna `True`.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}, donde cada
            valor contiene 'nombre', 'apellido', 'edad' y 'nota_final'.

    Returns:
        `True` si había alumnos registrados y se mostraron, o `False` si el
        diccionario estaba vacío.
    """
    if alumnos_vacios(alumnos):
        return False

    print("\nListado de alumnos:")
    for dni in alumnos:
        datos_alumno = alumnos[dni]
        print(f"\nDNI: {dni}")
        print(f"Nombre: {datos_alumno['nombre']}")
        print(f"Apellido: {datos_alumno['apellido']}")
        print(f"Edad: {datos_alumno['edad']}")
        print(f"Nota final: {datos_alumno['nota_final']}")

    return True