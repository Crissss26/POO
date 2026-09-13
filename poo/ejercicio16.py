#Clase DivisorFinder que: (1) tenga metodo encontrar_divisores(numero) que retorne una tupla con todos los divisores;
# (2) tenga metodo es_perfecto(numero) que retorne True si la suma de sus divisores (excepto el mismo) es igual a el;
#  (3) tenga metodo encontrar_multiples_divisores(*numeros) que retorne un diccionario {numero: tupla_divisores}.

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma_propios = sum(divisores[:-1])
        return suma_propios == numero

    def encontrar_multiples_divisores(self, *numeros):
        return {num: self.encontrar_divisores(num) for num in numeros}


df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.es_perfecto(12))
print(df.encontrar_multiples_divisores(6, 12))