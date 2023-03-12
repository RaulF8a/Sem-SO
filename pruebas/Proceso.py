class Proceso:
    def __init__(self, operacion: str, tiempoMaximoEstimado: str, idp: str, estado="Running", resultado=0) -> None:
        self._operacion = operacion
        self._resultado = 0
        self._idp = idp
        self._estado = estado

        # Tiempos
        self._tiempoMaximoEstimado = tiempoMaximoEstimado
        self._tiempo_transcurrido = 0
        self._tiempo_llegada = 0
        self._tiempo_espera = 0
        self._tiempo_servicio = 0
        self._tiempo_retorno = 0
        self._tiempo_respuesta = 0
        self._tiempo_finalizacion = 0
        self._tiempo_bloqueado = 0

        # Auxiliares y banderas.
        self._aux_tiempo_servicio = 0
        self._tiempo_respuesta_calculado = False

    @property
    def operacion(self) -> str:
        return self._operacion
    
    @operacion.setter
    def operacion(self, operacion: str) -> None:
        self._operacion = operacion
    
    @property
    def tiempoMaximoEstimado(self) -> str:
        return self._tiempoMaximoEstimado
    
    @tiempoMaximoEstimado.setter
    def tiempo(self, tiempoMaximoEstimado: str) -> None:
        self._tiempoMaximoEstimado = tiempoMaximoEstimado

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

    @property
    def tiempo_llegada(self) -> int:
        return self._tiempo_llegada

    @tiempo_llegada.setter
    def tiempo_llegada(self, tiempo_llegada:int) -> None:
        self._tiempo_llegada = tiempo_llegada
    
    @property
    def tiempo_espera(self) -> int:
        return self._tiempo_espera

    @tiempo_espera.setter
    def tiempo_espera(self, tiempo_espera:int) -> None:
        self._tiempo_espera = tiempo_espera
    
    @property
    def tiempo_servicio(self) -> int:
        return self._tiempo_servicio

    @tiempo_servicio.setter
    def tiempo_servicio(self, tiempo_servicio:int) -> None:
        self._tiempo_servicio = tiempo_servicio

    @property
    def tiempo_retorno(self) -> int:
        return self._tiempo_retorno

    @tiempo_retorno.setter
    def tiempo_retorno(self, tiempo_retorno:int) -> None:
        self._tiempo_retorno = tiempo_retorno
    
    @property
    def tiempo_respuesta(self) -> int:
        return self._tiempo_respuesta

    @tiempo_respuesta.setter
    def tiempo_respuesta(self, tiempo_respuesta:int) -> None:
        self._tiempo_respuesta = tiempo_respuesta
    
    @property
    def tiempo_bloqueado(self) -> int:
        return self._tiempo_bloqueado

    @tiempo_bloqueado.setter
    def tiempo_bloqueado(self, tiempo_bloqueado:int) -> None:
        self._tiempo_bloqueado = tiempo_bloqueado
    
    @property
    def tiempo_finalizacion(self) -> int:
        return self._tiempo_finalizacion

    @tiempo_finalizacion.setter
    def tiempo_finalizacion(self, tiempo_finalizacion:int) -> None:
        self._tiempo_finalizacion = tiempo_finalizacion

    @property
    def aux_tiempo_servicio(self) -> int:
        return self._aux_tiempo_servicio

    @aux_tiempo_servicio.setter
    def aux_tiempo_servicio(self, aux_tiempo_servicio:int) -> None:
        self._aux_tiempo_servicio = aux_tiempo_servicio
    
    @property
    def tiempo_respuesta_calculado(self) -> bool:
        return self._tiempo_respuesta_calculado

    @tiempo_respuesta_calculado.setter
    def tiempo_respuesta_calculado(self, tiempo_respuesta_calculado:bool) -> None:
        self._tiempo_respuesta_calculado = tiempo_respuesta_calculado

    def __eq__(self, other) -> bool:
        return self._idp == other._idp

    def __str__(self) -> str:
        return f"ID: {self._idp} TME: {self._tiempoMaximoEstimado} Operacion: {self._operacion} T.T.: {self._tiempo_transcurrido} Estado: {self._estado}"

