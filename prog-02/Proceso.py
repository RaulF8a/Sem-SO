class Proceso:
    def __init__(self, operacion: str, tiempo: str, idp: str) -> None:
        self.operacion = operacion
        self.tiempo = tiempo
        self.idp = idp
        self.tiempo_transcurrido = 0

    def __eq__(self, other) -> bool:
        return self.idp == other.idp

    def __str__(self) -> str:
        return f"ID: {self.idp} TME: {self.tiempo} Operacion: {self.operacion} T.T.: {self.tiempo_transcurrido}"

