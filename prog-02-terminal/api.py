from Proceso import Proceso
import random as rd

# Lista de procesos.
procesos = []
contadorID = 0
operadores = ['+', '-', '*', '/', '%']

# Obtener la longitud de la lista de procesos.
def procesos_count() -> str:
    return str(len(procesos))

# Crear la lista de procesos aleatoriamente.
def generar_lista_procesos(cantidad_procesos: int) -> None:
    while cantidad_procesos:
        procesos.append(Proceso(_generar_operacion(), _generar_tem(), _generar_id()))

        cantidad_procesos -= 1
    

def _generar_id() -> str:
    global contadorID

    contadorID += 1

    return str(contadorID)

def _generar_tem() -> str:
    return str(rd.randint(5, 16))

def _generar_operacion() -> str:
    operacion = ""

    valor1 = str(rd.randint(0,50))
    operador = operadores[rd.randint(0,len(operadores)-1)]
    valor2 = str(rd.randint(0,50))
    while valor2 == 0:
        valor2 = str(rd.randint(0,50))

    operacion = valor1 + operador + valor2

    return operacion

def obtener_lotes() -> list:
    # Se crea la lista de lotes.
    # Esta conformada por sublistas de cuatro procesos cada una.
    lotes = [procesos[i:i+4] for i in range(0, len(procesos), 4)]

    return lotes

def limpiar() -> None:
    procesos.clear()
