class Producto:
    def __init__(self, product_id, nombre, cantidad, precio):
        self._id = str(product_id)
        self._nombre = nombre
        self._cantidad = int(cantidad)
        self._precio = float(precio)

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        if int(cantidad) < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = int(cantidad)

    def set_precio(self, precio):
        if float(precio) < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(precio)

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
