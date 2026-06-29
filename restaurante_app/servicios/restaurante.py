from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que administra los productos y clientes del restaurante.
    """

    def __init__(self):
        # Listas para almacenar los objetos
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n========== PRODUCTOS ==========\n")

        for producto in self.productos:
            print(producto)
            print("-" * 40)

    def mostrar_clientes(self):
        print("\n========== CLIENTES ==========\n")

        for cliente in self.clientes:
            print(cliente)
            print("-" * 40)