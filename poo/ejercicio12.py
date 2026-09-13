#Clase ContadorFrecuencia que: (1) tenga metodo agregar_elemento(elemento) que guarde en un diccionario contando repeticiones;
# (2) tenga metodo elemento_mas_frecuente() que retorne el elemento con mayor frecuencia; (3) tenga metodo frecuencia_elemento(elemento)
#  que retorne cuantas veces aparece.
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))
print(cf.frecuencia_elemento("c"))