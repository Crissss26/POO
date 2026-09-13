#Clase AnalizadorTexto que: (1) tenga metodo agregar_palabra(palabra) que agregue la palabra a un conjunto
# (para evitar duplicados) y a una lista (para el orden); (2) tenga metodo contar_palabras() que retorne cuántas
# palabras únicas hay; (3) tenga metodo agregar_multiples(*args) que reutilice agregar_palabra para varios.
class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.historial_ordenado = []

    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.historial_ordenado.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())