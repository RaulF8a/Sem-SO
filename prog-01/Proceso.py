class Proceso:
    def __init__(self, nombre: str, operacion: str, tiempo: str, idp: str) -> None:
        self.nombre = nombre
        self.operacion = operacion
        self.tiempo = tiempo
        self.idp = idp

    def __eq__(self, other) -> bool:
        return self.idp == other.idp

    @property
    def get_nombre(self) -> str:
        return f"{self.nombre}"

    @property
    def get_operacion(self) -> str:
        return f"{self.operacion}"

    @property
    def get_tiempo(self) -> str:
        return f"{self.tiempo}"

    @property
    def get_idp(self) -> str:
        return f"{self.idp}"
