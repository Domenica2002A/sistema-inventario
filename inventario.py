from producto import Producto


class Inventario:
    def __init__(self):
        self._productos = []

    def _buscar_indice_por_id(self, product_id):
        for i, p in enumerate(self._productos):
            if p.get_id() == str(product_id):
                return i
        return -1

    def agregar_producto(self, producto):
        if self._buscar_indice_por_id(producto.get_id()) != -1:
            return False
        self._productos.append(producto)
        return True

    def eliminar_producto_por_id(self, product_id):
        idx = self._buscar_indice_por_id(product_id)
        if idx == -1:
            return False
        self._productos.pop(idx)
        return True

    def actualizar_producto(self, product_id, nueva_cantidad=None, nuevo_precio=None):
        idx = self._buscar_indice_por_id(product_id)
        if idx == -1:
            return False

        producto = self._productos[idx]

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        return True

    def buscar_productos_por_nombre(self, texto):
        resultados = []
        texto = texto.lower()
        for p in self._productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def obtener_todos(self):
        return self._productos

    def esta_vacio(self):
        return len(self._productos) == 0