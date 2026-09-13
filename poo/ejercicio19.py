#Clase CalculadorDistancia que: (1) tenga metodo distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia;
# (2) tenga metodo punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia;
#  (3) tenga un atributo lista para guardar todas las distancias calculadas.
import math
class CalculadorDistancia:
    def __init__(self):
        self.historial_distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.historial_distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        return min(puntos, key=lambda p: self.distancia_euclidiana(referencia, p))

cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))
mas_cercano = cd.punto_mas_cercano((0, 0), (5, 5), (1, 2), (3, 4))
print(mas_cercano)
print(cd.historial_distancias) 