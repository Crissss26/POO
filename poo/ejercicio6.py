#Clase AnalizadorNumeros que: (1) tenga metodo es_par(numero) que retorne True/False; (2) tenga metodo
# separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; (3)
# tenga metodo cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).
class AnalizadorNumeros:
    def __init__(self):
        self.ultimos_pares = []
        self.ultimos_impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        pares = []
        impares = []

        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)

        self.ultimos_pares = pares
        self.ultimos_impares = impares

        return {'pares': pares, 'impares': impares}

    def cantidad_pares_impares(self):
        return (len(self.ultimos_pares), len(self.ultimos_impares))


an = AnalizadorNumeros()
resultado = an.separar(1, 2, 3, 4, 5)
print(resultado)
print(an.cantidad_pares_impares())