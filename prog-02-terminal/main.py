from Proceso import Proceso
from api import *
from os import system
from time import sleep
import pprint
import keyboard

def main() -> None:
    lotes = generarProcesos()

    simular(lotes)

def generarProcesos() -> list:
    procesos = int(input("- Digita la cantidad de procesos: "))
    generar_lista_procesos(procesos)

    return obtener_lotes()

def simular(lotes: list) -> None:
    contadorGlobal = 0
    lotesPendientes = len(lotes)
    lotesTerminados = 0
    procesosTerminados = []
    
    # Recorrer la lista de lotes.
    for lote in lotes:
        lotesPendientes -= 1
        procesosLoteActual = lote.copy()
        procesosPendientes = procesosLoteActual.copy()
        contadorProcesos = 0
        
        imprimirCabecera(contadorGlobal, lotesPendientes, lotesTerminados)
        imprimirProcesosPendientes(procesosPendientes)

        while procesosPendientes:
            banderaError = False
            banderaInterrupcion = False

            proceso = procesosLoteActual[contadorProcesos]
            procesosPendientes.pop(0)

            while proceso.tiempoTranscurrido < int(proceso.tiempo):
                if keyboard.is_pressed('i') and proceso.estado == "Running":
                    procesosLoteActual.append(proceso)
                    procesosPendientes.append(proceso)
                    print ("\nSe solicito una Interrupcion")
                    sleep(1)
                    break

                elif keyboard.is_pressed('e') and proceso.estado == "Running":
                    banderaError = True
                    proceso.resultado = "Error"
                    proceso.tiempoTranscurrido = int(proceso.tiempo)
                    print ("\nSe solicito un Error")
                    sleep(1)

                elif keyboard.is_pressed('p') and proceso.estado == "Running":
                    proceso.estado = "Paused"
                    print ("\nSe solicito una Pausa")
                    print ("Presiona C para continuar...")
                    while keyboard.wait('c') and proceso.estado == "Paused":
                        pass

                else:
                    proceso.tiempoTranscurrido += 1
                    contadorGlobal += 1

                    imprimirBloque(contadorGlobal, lotesPendientes, lotesTerminados, procesosPendientes, proceso, procesosTerminados)
                    
                    sleep(1)
            
            if not banderaInterrupcion:
                if proceso.tiempoTranscurrido == int(proceso.tiempo):
                    if not banderaError:
                        proceso.resultado = str(realizarOperacion(proceso.operacion))
                        banderaError = False
                    procesosTerminados.append(proceso)
            
            contadorProcesos += 1
                               
        lotesTerminados += 1

        imprimirCabecera(contadorGlobal, lotesPendientes, lotesTerminados - 1)
        imprimirProcesosPendientes(procesosPendientes)
        print("")
        print(f"            ----      Proceso en Ejecucion      ----           ")
        print("")
        imprimirProcesosTerminados(procesosTerminados)     
    
def imprimirCabecera(contadorGlobal, lotesPendientes, lotesTerminados) -> None:
    system("cls")
    print(f"                      Contador Global: {contadorGlobal}           ")
    print(f"           Lotes Pendientes: {lotesPendientes}     N° Lote Actual: {lotesTerminados+1}") 

def imprimirProcesosPendientes(procesosLoteActual: list) -> None:
    print("")
    print(f"            ----      Procesos Pendientes      ---- ")
    print("")

    for proceso in procesosLoteActual:
        print(f"+ ID: {proceso.idp}      T.M.E.: {proceso.tiempo}      T.T.: {proceso.tiempoTranscurrido}")

def imprimirProcesoEjecucion(proceso: Proceso) -> None:
    print("")
    print(f"            ----      Proceso en Ejecucion      ----           ")
    print("")

    print(f"-> ID: {proceso.idp}     Operacion: {proceso.operacion}      T.M.E.: {proceso.tiempo}      T.T.: {proceso.tiempoTranscurrido}     T.R.: {int(proceso.tiempo) - int(proceso.tiempoTranscurrido)}")

def imprimirProcesosTerminados(procesosTerminados: list) -> None:
    print("")
    print(f"            ----      Procesos Terminados      ----           ")
    print("")

    for proceso in procesosTerminados:
        print(f"* ID: {proceso.idp}      Operacion: {proceso.operacion}      Resultado: {proceso.resultado}")

def imprimirBloque(contadorGlobal, lotesPendientes, lotesTerminados, procesosLoteActual, proceso, procesosTerminados) -> None:
    imprimirCabecera(contadorGlobal, lotesPendientes, lotesTerminados)
    imprimirProcesosPendientes(procesosLoteActual)
    imprimirProcesoEjecucion(proceso)
    imprimirProcesosTerminados(procesosTerminados)

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


