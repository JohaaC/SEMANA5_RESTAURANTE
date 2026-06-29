class Producto:
    """
    Clase que representa un producto del restaurante.
    """

    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        cantidad: int,
        disponible: bool
    ):
        # Atributos del producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Cantidad: {self.cantidad}\n"
            f"Estado: {estado}"
        )