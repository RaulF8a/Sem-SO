from Proceso import Proceso
import random as rd

# Lista de procesos.
procesos = []
contadorID = 0
operadores = ['+', '-', '*', '/', '%']

# Obtener la longitud de la lista de procesos.
def procesos_count() -> str:
    return str(len(procesos))

# Agregar proceso. Se reciben como parametros los datos que debe tener.
def generar_lista_procesos(cantidad_procesos: int) -> None:
    while cantidad_procesos:
        procesos.append(Proceso(_generar_operacion(), _generar_tem(), _generar_id()))

        cantidad_procesos -= 1
    
    for proceso in procesos:
        print(proceso)

def _generar_id() -> str:
    global contadorID

    contadorID += 1

    return str(contadorID)

def _generar_tem() -> str:
    return str(rd.randint(1, 16))

def _generar_operacion() -> str:
    operacion = ""

    # Valor 1
    operacion += str(rd.randint(0,50))
    # Operador
    operacion += operadores[rd.randint(0,len(operadores)-1)]
    # Valor 2
    operacion += str(rd.randint(1,50))

    return operacion

def obtener_lotes() -> list:
    # Se crea la lista de lotes.
    # Esta conformada por sublistas de cuatro procesos cada una.
    lotes = [procesos[i:i+4] for i in range(0, len(procesos), 4)]

    return lotes

def limpiar() -> None:
    procesos.clear()
