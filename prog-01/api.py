from Proceso import Proceso

# Lista de procesos.
procesos = []

# Obtener la longitud de la lista de procesos.
def procesos_count() -> str:
    return str(len(procesos))

# Agregar proceso. Se reciben como parametros los datos que debe tener.
def agregar_proceso(nombre: str, operacion: str, tiempo: str, idp: str) -> tuple:
    # Se valida que se hayan llenado todos los campos.
    if not nombre or not operacion or not tiempo or not idp:
        return 4, "Debes llenar todos los campos."

    # Validar si el ID ya existe.
    if not validar_id(idp):
        return 1, "El ID del proceso ya existe."

    # Validar division y modulo entre 0.
    if not validar_operacion(operacion):
        return 2, "Operacion no valida."

    # Validar que el tiempo sea mayor a cero.
    if int(tiempo) <= 0:
        return 3, "El tiempo debe ser mayor a cero."

    # Si no hubo errores, se agrega el proceso a la lista.
    procesos.append(Proceso(nombre, operacion, tiempo, idp))
    return 0, ""


def validar_id(idp: str) -> bool:
    # Creamos un objeto de la clase Proceso con el id.
    # El operador = esta sobrecargado para que compare unicamente el id de un proceso con otro.
    aux = Proceso("", "", "", idp)

    # Iteramos sobre la lista de procesos para ver si ya existe el ID.
    if aux not in procesos:
        return True

    return False


def validar_operacion(operacion: str) -> bool:
    for i in range(len(operacion)):
        # Buscamos el operador / o % y validamos que el siguiente digito no sea cero.
        if operacion[i] == '/' or operacion[i] == '%':
            if operacion[i + 1] == '0':
                return False

    return True


def obtener_lotes() -> list:
    # Se crea la lista de lotes.
    # Esta conformada por sublistas de cuatro procesos cada una.
    lotes = [procesos[i:i + 4] for i in range(0, len(procesos), 4)]

    return lotes


def limpiar() -> None:
    procesos.clear()
