class Proceso:
    def __init__(self, operacion: str, tiempo: str, idp: str, estado="Running", resultado=0) -> None:
        self._operacion = operacion
        self._resultado = 0
        self._tiempo = tiempo
        self._idp = idp
        self._tiempo_transcurrido = 0
        self._estado = estado

    @property
    def operacion(self) -> str:
        return self._operacion
    
    @operacion.setter
    def operacion(self, operacion: str) -> None:
        self._operacion = operacion
    
    @property
    def tiempo(self) -> str:
        return self._tiempo
    
    @tiempo.setter
    def tiempo(self, tiempo: str) -> None:
        self._tiempo = tiempo

    @property
    def idp(self) -> str:
        return self._idp

    @idp.setter
    def idp(self, idp: str) -> None:
        self._idp = idp

    @property
    def tiempoTranscurrido(self) -> str:
        return self._tiempo_transcurrido

    @tiempoTranscurrido.setter
    def tiempoTranscurrido(self, tiempoTranscurrido: int) -> None:
        self._tiempo_transcurrido = tiempoTranscurrido

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, estado: str) -> None:
        self._estado = estado

    @property
    def resultado(self) -> float:
        return self._resultado
    
    @resultado.setter
    def resultado(self, resultado: str) -> None:
        self._resultado = resultado

    def __eq__(self, other) -> bool:
        return self._idp == other._idp

    def __str__(self) -> str:
        return f"ID: {self._idp} TME: {self._tiempo} Operacion: {self._operacion} T.T.: {self._tiempo_transcurrido} Estado: {self._estado}"

