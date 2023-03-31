
PAGINAS_POR_FRAME = 5
PAGINA_LIBRE = -1
SO = -2
CANTIDAD_FRAMES = 40

class Frame:
    def __init__(self) -> None:
        self.espacioDisponible = PAGINAS_POR_FRAME
        self.procesoQueUsaElEspacio = ""
        self.estadoDelProceso = ""

class Memoria:
    def __init__(self) -> None:
        self.memoria: list[Frame] = []

        for i in range(CANTIDAD_FRAMES):
            self.memoria.append(Frame())

    def memoriaLlena(self) -> bool:
        framesLlenos = 0

        for i in range(CANTIDAD_FRAMES - 2):
            if self.memoria[i].espacioDisponible < PAGINAS_POR_FRAME:
                framesLlenos += 1
        
        return framesLlenos == CANTIDAD_FRAMES - 2

    def cantidadFramesDisponibles(self) -> int:
        framesDisponibles: int = 0

        for i in range(CANTIDAD_FRAMES - 2):
            # Solo si un frame tiene todas sus paginas sin usar, estara disponible.
            if self.memoria[i].espacioDisponible == PAGINAS_POR_FRAME:
                framesDisponibles += 1

        return framesDisponibles

    def llenarFrames(self, tamanio: int, frames: int, id: str, estado: str) -> None:
        framesLlenados = 0
        
        for i in range(CANTIDAD_FRAMES - 2):
            # Validamos si el frame actual de la memoria tiene espacio y si el proceso aun requiere frames.
            if (self.memoria[i].espacioDisponible == PAGINAS_POR_FRAME and framesLlenados < frames):
                if (framesLlenados == frames - 1):
                    if (tamanio % PAGINAS_POR_FRAME != 0):
                        self.memoria[i].espacioDisponible -= (tamanio % PAGINAS_POR_FRAME)
                    else:
                        self.memoria[i].espacioDisponible = 0
                else:
                    self.memoria[i].espacioDisponible = 0

                # print(f"frame {i+1} tiene {self.memoria[i].espacioDisponible} paginas libres.")

                self.memoria[i].procesoQueUsaElEspacio = id
                self.memoria[i].estadoDelProceso = estado
                framesLlenados += 1

            print(f"Frame {i+1} tiene {self.memoria[i].espacioDisponible} paginas libres.")

    def cambiarEstadoProceso(self, id: str, estado: str) -> None:
        for i in range(CANTIDAD_FRAMES - 2):
            if self.memoria[i].procesoQueUsaElEspacio == id:
                self.memoria[i].estadoDelProceso = estado

    def liberarFrames(self, id: str) -> None:
        for i in range(CANTIDAD_FRAMES - 2):
            if self.memoria[i].procesoQueUsaElEspacio == id:
                self.memoria[i].procesoQueUsaElEspacio = ""
                self.memoria[i].estadoDelProceso = ""
                self.memoria[i].espacioDisponible = PAGINAS_POR_FRAME

    def lenght(self) -> int:
        return len(self.memoria)          
