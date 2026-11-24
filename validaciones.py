def validar_textos(texto: str) -> bool:
    """Valida que una cadena de texto no esté vacía y contenga solo letras y espacios.

    Recorre cada carácter de `texto` para verificar que sea una letra
    minúscula (`'a'`–`'z'`), mayúscula (`'A'`–`'Z'`) o espacio (`' '`), y
    finalmente verifica con `strip() != ""` que no esté vacía ni formada solo
    por espacios.

    Args:
        texto: Cadena de texto ingresada por el usuario.

    Returns:
        True si el texto cumple con los caracteres permitidos y no está vacío
        tras eliminar espacios extremos, False en caso contrario.
    """
    for i in range(len(texto)):
        caracter = texto[i]
        es_minuscula = "a" <= caracter <= "z"
        es_mayuscula = "A" <= caracter <= "Z"
        tiene_espacio = caracter == " "

        if not (es_minuscula or es_mayuscula or tiene_espacio):
            return False

    return texto.strip() != ""


def validar_entero_no_negativo(texto: str) -> bool:
    """Valida que una cadena represente un número entero no negativo.

    Verifica que el texto no esté vacío y que todos sus caracteres sean
    dígitos numéricos entre `'0'` y `'9'`, mostrando un mensaje de error por
    consola si no cumple alguna condición.

    Args:
        texto: Cadena de texto a validar.

    Returns:
        True si la cadena no está vacía y todos sus caracteres están entre
        `'0'` y `'9'`, o False en caso contrario.
    """
    if texto == "":
        print("\nError, no se puede ingresar un valor vacío.")
        return False

    for i in range(len(texto)):
        if texto[i] < "0" or texto[i] > "9":
            print("\nError, el valor ingresado debe ser un entero positivo.")
            return False

    return True


def pedir_texto(mensaje: str) -> str:
    """Solicita una cadena de texto por consola hasta que sea válida.

    Muestra `mensaje`, lee la entrada del usuario y repite la solicitud
    mientras `validar_textos` indique que el texto no es válido.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar el dato.

    Returns:
        La cadena ingresada por el usuario una vez validada.
    """
    texto = input(mensaje)
    while not validar_textos(texto):
        print("Error: el texto no puede estar vacío ni contener caracteres inválidos.")
        texto = input(mensaje)
    return texto


def pedir_entero(mensaje: str) -> int:
    """Solicita un número entero no negativo por consola hasta que sea válido.

    Muestra `mensaje`, lee la entrada sin espacios extremos con `strip()` y
    repite la solicitud mientras `validar_entero_no_negativo` retorne False.
    Finalmente convierte la cadena validada a entero.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar el número.

    Returns:
        El número entero no negativo ingresado y validado.
    """
    texto = input(mensaje).strip()
    while not validar_entero_no_negativo(texto):
        texto = input(mensaje).strip()
    return int(texto)


def pedir_dni(mensaje: str) -> int:
    """Solicita y valida un número de DNI de entre 7 y 8 dígitos por consola.

    Utiliza `pedir_entero` para obtener un entero no negativo y repite la
    solicitud mientras el valor esté fuera del rango `1000000` a `99999999`.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar el DNI.

    Returns:
        El número de DNI validado como entero dentro del rango de 7 u 8 dígitos.
    """
    validar = pedir_entero(mensaje)

    while validar < 1000000 or validar > 99999999:
        print("Error: el DNI debe tener entre 7 y 8 dígitos.")
        validar = pedir_entero(mensaje)
    return validar


def pedir_edad(mensaje: str) -> int:
    """Solicita y valida la edad de un alumno entre 4 y 80 años por consola.

    Utiliza `pedir_entero` para obtener un número entero no negativo y repite la
    solicitud mientras la edad esté fuera del rango de 4 a 80 años.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar la edad.

    Returns:
        La edad validada como entero dentro del rango de 4 a 80.
    """
    edad = pedir_entero(mensaje)
    while edad < 4 or edad > 80:
        print("Error: la edad debe estar entre 4 y 80 años.")
        edad = pedir_entero(mensaje)
    return edad


def pedir_nota(mensaje: str) -> float:
    """Solicita y valida la nota final de un alumno entre 0 y 10 por consola.

    Utiliza `pedir_entero` para obtener un número entero no negativo y repite
    la solicitud mientras la nota esté fuera del rango de 0 a 10.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar la nota final.

    Returns:
        La nota final validada como flotante dentro del rango de 0 a 10.
    """
    nota_final = pedir_entero(mensaje)
    while nota_final < 0 or nota_final > 10:
        print("Error: la nota final debe estar entre 0 y 10.")
        nota_final = pedir_entero(mensaje)
    return float(nota_final)
