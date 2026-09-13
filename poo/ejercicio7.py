#Clase GestorTemperatura que: (1) tenga metodo registrar_temperatura(temp) que guarde en una lista;
# (2) tenga metodo minima()`, `maxima()`, `promedio() que calculen estadísticas; (3) tenga metodo registrar_multiples(*temps)
#  que reutilice el registro para varias temperaturas.
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        if not self.temperaturas:
            return None
        return min(self.temperaturas)

    def maxima(self):
        if not self.temperaturas:
            return None
        return max(self.temperaturas)

    def promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())
print(f"Mínima: {gt.minima()}, Máxima: {gt.maxima()}")