#Clase Inventario que: (1) tenga metodo agregar_stock(producto, cantidad) que guarde en un diccionario;
# (2) tenga metodo restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente;
#  (3) tenga metodo productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [
            prod for prod, cant in self.stock.items()
            if cant < minimo
        ]


inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
inv.stock["pan"] = 10
print(inv.productos_bajo_stock(15))