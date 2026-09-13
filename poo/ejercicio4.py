#Clase CarroCompras que: (1) tenga metodo agregar_articulo(nombre, precio) que guarde en un diccionario
#{nombre: precio}; (2) tenga metodo total_carrito() que retorne la suma de todos los precios; (3) tenga metodo
# articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [
            nombre for nombre, precio in self.articulos.items()
            if precio_min <= precio <= precio_max
        ]


c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
print(c.total_carrito())
print(c.articulos_por_rango(2.00, 2.80))