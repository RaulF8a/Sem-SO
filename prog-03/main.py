from Proceso import Proceso
from api import *
from os import system
from time import sleep
import keyboard

def main() -> None:
    procesos = generarProcesos()

    simular(procesos)

def generarProcesos() -> list:
    procesos = int(input("- Digita la cantidad de procesos: "))
    generar_lista_procesos(procesos)

    return obtener_lista_procesos()

def simular(procesos: list) -> None:
    MAXIMA_CANTIDAD_PROCESOS : int = 4
    MAXIMO_TIEMPO_BLOQUEADO : int = 8
    PROCESO_NULO : Proceso = Proceso ("0+0", "0", "0")
    procesosEnMemoria : list = []
    procesosBloqueados : list = []
    procesosTerminados : list = []
    contadorGlobal : int = 0
    procesoActual : Proceso

    # Cargar los primeros cuatro procesos a la lista de listos y se eliminan de los nuevos.
    procesosListos = procesos[:4]
    procesos = procesos[4:]

    # Actualizamos la lista de prcoesos en memoria.
    procesosEnMemoria = procesosListos.copy()

    while True:
        banderaError = False
        banderaInterrupcion = False
        procesoActual = PROCESO_NULO

        # Si ya no quedan procesos en la memoria, entonces terminamos el bucle.
        if not procesos and not procesosEnMemoria:
            break
        
        # Mostramos el contador global.
        imprimirCabecera (contadorGlobal, len(procesos))

        # Mostramos los procesos listos.
        imprimirProcesosListos(procesosListos)

        # Cargamos el procesos actual y lo eliminamos de los listos.
        if len(procesosListos) > 0:
            procesoActual = procesosListos[0]
            procesosListos.pop(0)

        while procesoActual.tiempoTranscurrido < int(procesoActual.tiempo):
            # Verificamos si el tiempo de respuesta ya ha sido calculado para el proceso actual.
            if not procesoActual.tiempo_respuesta_calculado:
                procesoActual.tiempo_respuesta = contadorGlobal - procesoActual.tiempo_llegada
                procesoActual.tiempo_respuesta_calculado = True

            if keyboard.is_pressed('i') and procesoActual.estado == "Running":
                banderaInterrupcion = True

                # Si un proceso se interrumpio, es enviado a la lista de bloqueados.
                procesosBloqueados.append(procesoActual)

                print ("\nSe solicito una Interrupcion")
                sleep(1)
                break

            elif keyboard.is_pressed('e') and procesoActual.estado == "Running":
                banderaError = True

                procesoActual.resultado = "Error"
                procesoActual.aux_tiempo_servicio = procesoActual.tiempoTranscurrido
                procesoActual.tiempoTranscurrido = int(procesoActual.tiempoMaximoEstimado)

                print ("\nSe solicito un Error")
                sleep(1)

            elif keyboard.is_pressed('p') and procesoActual.estado == "Running":
                procesoActual.estado = "Paused"

                print ("\nSe solicito una Pausa")
                print ("Presiona C para continuar...")

                while keyboard.wait('c') and procesoActual.estado == "Paused":
                    pass

            else:
                procesoActual.tiempoTranscurrido += 1
                contadorGlobal += 1

                # Aumentamos el tiempo de los procesos bloqueados.
                if procesosBloqueados:
                    for bloqueado in procesosBloqueados:
                        bloqueado.tiempo_bloqueado += 1
                        # bloqueado.tiempo_espera += 1

                        if (bloqueado.tiempo_bloqueado % MAXIMO_TIEMPO_BLOQUEADO) == 0:
                            procesosBloqueados.remove(bloqueado)
                            procesosListos.append(bloqueado)
                            # bloqueado.tiempo_espera += 1
                
                # Aumentamos el tiempo de espera de los procesos listos.
                # for listo in procesosListos:
                #     listo.tiempo_espera += 1

                imprimirBloque(contadorGlobal, procesos, procesosListos, procesoActual, procesosBloqueados, procesosTerminados)
                
                sleep(1)
        
        # Si el procesoa actual es igual al proceso nulo, entonces solo quedaba un proceso y esta bloqueado.
        if procesosBloqueados and procesoActual == PROCESO_NULO:
            imprimirBloque(contadorGlobal, procesos, procesosListos, procesoActual, procesosBloqueados, procesosTerminados)

            for bloqueado in procesosBloqueados:
                bloqueado.tiempo_bloqueado += 1

                if (bloqueado.tiempo_bloqueado % MAXIMO_TIEMPO_BLOQUEADO) == 0:
                    procesosBloqueados.remove(bloqueado)
                    procesosListos.append(bloqueado)
            
            contadorGlobal += 1
            sleep(1)
            continue
        
        # Verificamos si no se realizo una interrupcion.
        if not banderaInterrupcion:
            # Si el tiempo transcurrido es igual al estimado, entonces el proceso ya termino su ejecucion.
            if procesoActual.tiempoTranscurrido == int(procesoActual.tiempoMaximoEstimado):
                # Evaluamos si se termino normalmente o fue por un error.
                if not banderaError:
                    procesoActual.resultado = str(realizarOperacion(procesoActual.operacion))
                    banderaError = False
                    # Asignamos el tiempo de servicio.
                    procesoActual.tiempo_servicio = procesoActual.tiempoMaximoEstimado
                else:
                    # Asignamos el tiempo de servicio. Cuando ocurrio un error, sera igual al tiempo transcurrido.
                    procesoActual.tiempo_servicio = procesoActual.aux_tiempo_servicio

                # Asignamos el tiempo de finalizacion.
                procesoActual.tiempo_finalizacion = contadorGlobal
                # Asignamos el tiempo de retorno del proceso actual.
                procesoActual.tiempo_retorno = contadorGlobal - procesoActual.tiempo_llegada
                procesoActual.tiempo_espera = int(procesoActual.tiempo_retorno) - int(procesoActual.tiempo_servicio)
                procesosTerminados.append(procesoActual)
                
                # Eliminamos el proceso actual de la memoria.
                procesosEnMemoria.remove(procesoActual)

                # Ponemos su estado en Terminado.
                procesoActual.estado = "Terminado"

        # # Verificamos que aun existan procesos nuevos.
        # Revisamos si aun hay cuatro procesos en memoria. Si no, se agregan más.
        if len(procesosEnMemoria) < MAXIMA_CANTIDAD_PROCESOS and procesos:
            for i in range(len(procesosEnMemoria), MAXIMA_CANTIDAD_PROCESOS):
                # Se asigna el tiempo de llegada al proceso que entro al sistema.
                procesos[0].tiempo_llegada = contadorGlobal
                procesosEnMemoria.append(procesos[0])
                procesosListos.append(procesos[0])

                procesos.pop(0)
    
    imprimirResumen(procesosTerminados)


def imprimirCabecera(contadorGlobal: int, procesosNuevos: int) -> None:
    system("cls")
    print(f"               Contador Global:  {contadorGlobal}       Procesos Nuevos: {procesosNuevos}    ")

def imprimirProcesosListos(procesosListos: list) -> None:
    print("")
    print(f"                 |----        Procesos Listos        ----| ")
    print("")

    for proceso in procesosListos:
        print(f"+ ID: {proceso.idp}      T.M.E.: {proceso.tiempoMaximoEstimado}      T.T.: {proceso.tiempoTranscurrido}")

def imprimirProcesoEjecucion(proceso: Proceso) -> None:
    print("")
    print(f"                 |----      Proceso en Ejecucion     ----|           ")
    print("")

    if proceso.idp != "0":
        print(f"-> ID: {proceso.idp}     Operacion: {proceso.operacion}      T.M.E.: {proceso.tiempoMaximoEstimado}      T.T.: {proceso.tiempoTranscurrido}     T.R.: {int(proceso.tiempoMaximoEstimado) - int(proceso.tiempoTranscurrido)}")

def imprimirProcesosTerminados(procesosTerminados: list) -> None:
    print("")
    print(f"                 |----      Procesos Terminados      ----|           ")
    print("")

    for proceso in procesosTerminados:
        print(f"* ID: {proceso.idp}      Operacion: {proceso.operacion}      Resultado: {proceso.resultado}")

def imprimirProcesosBloqueados(procesosBloqueados: list) -> None:
    print("")
    print(f"                 |----      Procesos Bloqueados      ----|           ")
    print("")

    for bloqueado in procesosBloqueados:
        print(f"* ID: {bloqueado.idp}      T.B.: {bloqueado.tiempo_bloqueado} ")

def imprimirBloque(contadorGlobal, procesosNuevos: list, procesosListos: list, proceso: Proceso, procesosBloqueados: list, procesosTerminados: list) -> None:
    imprimirCabecera(contadorGlobal, len(procesosNuevos))
    imprimirProcesosListos(procesosListos)
    imprimirProcesoEjecucion(proceso)
    imprimirProcesosBloqueados(procesosBloqueados)
    imprimirProcesosTerminados(procesosTerminados)

def imprimirResumen(procesosTerminados: list) -> None:
    system("cls")

    print(f"                                                 |----          Resumen         ----|           ")
    print("")

    for proceso in procesosTerminados:
        print(f"* ID: {proceso.idp}   Operacion: {proceso.operacion}   Resultado: {proceso.resultado}   T.M.E.: {proceso.tiempoMaximoEstimado}   T.Lleg.: {proceso.tiempo_llegada}   T.Fin.: {proceso.tiempo_finalizacion}   T.Ret.: {proceso.tiempo_retorno}   T.Resp.: {proceso.tiempo_respuesta}   T.Esp.: {proceso.tiempo_espera}   T.Serv.: {proceso.tiempo_servicio}")


def realizarOperacion(operacion: str) -> float:
    # Separamos lo que hay antes y despues del operador para obtener los valores.
    for i in range(len(operacion)):
        if operacion[i] == '+' or operacion[i] == '-' or operacion[i] == '*' or operacion[i] == '/' or operacion[i] == '%':
            operador = operacion[i]
            valor1 = float(operacion[:i])
            valor2 = float(operacion[i+1:])

    # Retornamos el resultado de la operacion.
    if operador == "+":
        return valor1 + valor2
    elif operador == "-":
        return valor1 - valor2
    elif operador == "*":
        return valor1 * valor2
    elif operador == "/":
        return round(valor1 / valor2, 2)
    else:
        return valor1 % valor2

if __name__ == "__main__":
    main()
