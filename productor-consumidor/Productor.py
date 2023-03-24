class Productor:
    def __init__(self) -> None:
        self._estado = 0
        self._posicionActual = 0

    def producir(self) -> bool:
        return True

    @property
    def estado(self) -> int:
        return self._estado
    
    @estado.setter
    def estado(self, estado: int) -> None:
        self._estado = estado

    @property
    def posicionActual(self) -> int:
        return self._posicionActual
    
    @posicionActual.setter
    def posicionActual(self, posicionActual: int) -> None:
        self._posicionActual = posicionActual