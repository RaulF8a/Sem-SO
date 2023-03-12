class Proceso:
    def __init__(self, operacion: str, tiempo_maximo_estimado: str, idp: str, estado="Nuevo", resultado="0") -> None:
        self._operacion = operacion
        self._resultado = "N/A"
        self._idp = idp
        self._estado = estado

        # Tiempos
        self._tiempo_maximo_estimado = tiempo_maximo_estimado
        self._tiempo_restante = "0"
        self._tiempo_transcurrido = "N/A"
        self._tiempo_bloqueado = "N/A"

        self._tiempo_llegada = "N/A"
        self._tiempo_espera = "N/A"
        self._tiempo_servicio = "N/A"
        self._tiempo_retorno = "N/A"
        self._tiempo_respuesta = "N/A"
        self._tiempo_finalizacion = "N/A"
        
        # Auxiliares y banderas.
        self._aux_tiempo_servicio = "0"
        self._tiempo_respuesta_calculado = False

    @property
    def operacion(self) -> str:
        return self._operacion
    
    @operacion.setter
    def operacion(self, operacion: str) -> None:
        self._operacion = operacion
    
    @property
    def tiempo_maximo_estimado(self) -> str:
        return self._tiempo_maximo_estimado
    
    @tiempo_maximo_estimado.setter
    def tiempo_maximo_estimado(self, tiempo_maximo_estimado: str) -> None:
        self._tiempo_maximo_estimado = tiempo_maximo_estimado

    @property
    def idp(self) -> str:
        return self._idp

    @idp.setter
    def idp(self, idp: str) -> None:
        self._idp = idp

    @property
    def tiempo_transcurrido(self) -> str:
        return self._tiempo_transcurrido

    @tiempo_transcurrido.setter
    def tiempo_transcurrido(self, tiempo_transcurrido: str) -> None:
        self._tiempo_transcurrido = tiempo_transcurrido

    @property
    def tiempo_restante(self) -> str:
        return self._tiempo_restante

    @tiempo_restante.setter
    def tiempo_restante(self, tiempo_restante: str) -> None:
        self._tiempo_restante = tiempo_restante

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, estado: str) -> None:
        self._estado = estado

    @property
    def resultado(self) -> str:
        return self._resultado
    
    @resultado.setter
    def resultado(self, resultado: str) -> None:
        self._resultado = resultado

    @property
    def tiempo_llegada(self) -> str:
        return self._tiempo_llegada

    @tiempo_llegada.setter
    def tiempo_llegada(self, tiempo_llegada:str) -> None:
        self._tiempo_llegada = tiempo_llegada
    
    @property
    def tiempo_espera(self) -> str:
        return self._tiempo_espera

    @tiempo_espera.setter
    def tiempo_espera(self, tiempo_espera:str) -> None:
        self._tiempo_espera = tiempo_espera
    
    @property
    def tiempo_servicio(self) -> str:
        return self._tiempo_servicio

    @tiempo_servicio.setter
    def tiempo_servicio(self, tiempo_servicio:str) -> None:
        self._tiempo_servicio = tiempo_servicio

    @property
    def tiempo_retorno(self) -> str:
        return self._tiempo_retorno

    @tiempo_retorno.setter
    def tiempo_retorno(self, tiempo_retorno:str) -> None:
        self._tiempo_retorno = tiempo_retorno
    
    @property
    def tiempo_respuesta(self) -> str:
        return self._tiempo_respuesta

    @tiempo_respuesta.setter
    def tiempo_respuesta(self, tiempo_respuesta:str) -> None:
        self._tiempo_respuesta = tiempo_respuesta
    
    @property
    def tiempo_bloqueado(self) -> str:
        return self._tiempo_bloqueado

    @tiempo_bloqueado.setter
    def tiempo_bloqueado(self, tiempo_bloqueado:str) -> None:
        self._tiempo_bloqueado = tiempo_bloqueado
    
    @property
    def tiempo_finalizacion(self) -> str:
        return self._tiempo_finalizacion

    @tiempo_finalizacion.setter
    def tiempo_finalizacion(self, tiempo_finalizacion:str) -> None:
        self._tiempo_finalizacion = tiempo_finalizacion

    @property
    def aux_tiempo_servicio(self) -> str:
        return self._aux_tiempo_servicio

    @aux_tiempo_servicio.setter
    def aux_tiempo_servicio(self, aux_tiempo_servicio:str) -> None:
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
        return f"ID: {self._idp} TME: {self._tiempo_maximo_estimado} Operacion: {self._operacion} T.T.: {self._tiempo_transcurrido} Estado: {self._estado}"

