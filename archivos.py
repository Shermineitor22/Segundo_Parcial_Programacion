import json


def cargar_alumnos() -> dict[int, dict]:
    """Carga los datos de alumnos desde el archivo JSON o retorna un diccionario vacío.

    Lee y deserializa el contenido de `alumnos.json` mediante `json.load` con
    codificación `utf-8`. Si el contenido cargado está vacío, retorna `{}`; de
    lo contrario, actualiza el diccionario convirtiendo las claves a `int` y lo
    devuelve.

    Returns:
        El diccionario cargado desde `alumnos.json` con claves enteras, o `{}`
        si no contiene datos.
    """
    with open("alumnos.json", "r", encoding="utf-8") as archivo:
        alumnos = json.load(archivo)

    if len(alumnos) == 0:
        return alumnos

    for dni in list(alumnos.keys()):
        alumnos[int(dni)] = alumnos.pop(dni)

    return alumnos


def guardar_alumnos(alumnos: dict[int, dict]) -> None:
    """Guarda el diccionario de alumnos en el archivo JSON.

    Escribe el contenido formateado del diccionario `alumnos` en `alumnos.json`
    con codificación `utf-8` (incluyendo `{}` si no hay registros) y retorna
    `None`.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        None.
    """
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4)

    return None
