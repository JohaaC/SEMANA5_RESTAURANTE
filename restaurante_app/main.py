from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear el restaurante
restaurante = Restaurante()

# Crear productos
producto1 = Producto(
    "Pizza Familiar",
    "Comida",
    12.50,
    20,
    True
)

producto2 = Producto(
    "Jugo Natural",
    "Bebida",
    3.25,
    35,
    True
)

# Crear clientes
cliente1 = Cliente(
    "María López",
    25,
    "maria@gmail.com",
    True
)

cliente2 = Cliente(
    "Carlos Pérez",
    30,
    "carlos@gmail.com",
    False
)

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()