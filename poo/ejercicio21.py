#Clase AnalizadorPatrones que: (1) tenga metodo encontrar_palabras(texto, patron) que busque palabras que inicien con
# el patrón y retorne una lista; (2) tenga metodo agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]};
#  (3) tenga metodo palabras_unicas() usando un conjunto.
class AnalizadorPatrones:
    def __init__(self):
        self.texto_guardado = ""

    def encontrar_palabras(self, texto, patron):
        self.texto_guardado = texto
        palabras = texto.split()
        return [palabra for palabra in palabras if palabra.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        self.texto_guardado = texto
        palabras = texto.split()
        grupos = {}

        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self, texto=None):
        target = texto if texto is not None else self.texto_guardado
        return set(target.split())


ap = AnalizadorPatrones()
print(ap.encontrar_palabras("el gato está aquí", "es"))
print(ap.agrupar_por_longitud("el gato está aquí"))
print(ap.palabras_unicas("el gato el perro"))