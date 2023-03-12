from Proceso import Proceso
import random as rd

# Lista de procesos.
_procesos = []
_procesosTabla = []
_contadorID = 0
_contadorGlobal = 0
_operadores = ['+', '-', '*', '/', '%']

# Obtener la longitud de la lista de procesos.
def procesos_count() -> str:
    return str(len(_procesos))

# Crear la lista de procesos aleatoriamente.
def generar_lista_procesos(cantidad_procesos: int) -> None:
    while cantidad_procesos:
        crear_proceso()

        cantidad_procesos -= 1
    
def crear_proceso() -> Proceso:
    proceso = Proceso(_generar_operacion(), _generar_tem(), _generar_id())
    _procesos.append(proceso)

    return proceso

def _generar_id() -> str:
    global _contadorID

    _contadorID += 1

    return str(_contadorID)

def _generar_tem() -> str:
    return str(rd.randint(5, 16))

def _generar_operacion() -> str:
    operacion = ""

    valor1 = str(rd.randint(0,50))
    operador = _operadores[rd.randint(0,len(_operadores)-1)]
    valor2 = str(rd.randint(0,50))

    if operador == '%' or operador == '/':
        while valor2 == "0":
            valor2 = str(rd.randint(0,50))

    operacion = valor1 + operador + valor2

    return operacion

def obtener_lista_procesos() -> list:
    return _procesos

def crearProcesosTabla(contadorGlobal: int) -> None:
    global _procesosTabla
    global _contadorGlobal
    _procesosTabla = _procesos.copy()
    _contadorGlobal = contadorGlobal

def obtenerProcesosTabla() -> tuple[list, int]:
    return _procesosTabla, _contadorGlobal


def limpiar() -> None:
    _procesos.clear()
