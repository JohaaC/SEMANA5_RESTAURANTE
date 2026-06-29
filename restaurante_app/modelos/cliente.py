class Cliente:
    """
    Clase que representa un cliente del restaurante.
    """

    def __init__(
        self,
        nombre: str,
        edad: int,
        correo: str,
        cliente_frecuente: bool
    ):
        # Atributos del cliente
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.cliente_frecuente = cliente_frecuente

    def __str__(self):
        tipo_cliente = (
            "Cliente frecuente"
            if self.cliente_frecuente
            else "Cliente ocasional"
        )

        return (
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Correo: {self.correo}\n"
            f"Tipo: {tipo_cliente}"
        )