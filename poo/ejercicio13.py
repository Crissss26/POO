#Clase SelectorRango que: (1) tenga metodo crear_rango(inicio, fin) que retorne una tupla con números en ese rango;
# (2) tenga metodo elementos_en_multiples_rangos(*rangos) que reciba multiples tuplas (inicio,fin)
#  y retorne una lista combinada sin duplicados usando un conjunto.
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos_unicos = set()

        for inicio, fin in rangos:
            rango_tupla = self.crear_rango(inicio, fin)
            elementos_unicos.update(rango_tupla)
        return sorted(list(elementos_unicos))

sr = SelectorRango()
print(sr.crear_rango(1, 3))
resultado = sr.elementos_en_multiples_rangos((1, 3), (2, 4))
print(resultado)