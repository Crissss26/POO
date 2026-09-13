#Clase CodificadorCesar que: (1) tenga metodo codificar_letra(letra, desplazamiento) que retorne la letra desplazada
# en el alfabeto (usar operador %); (2) tenga metodo codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra;
#  (3) tenga un diccionario como atributo para historial de codificaciones.
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        palabra_codificada = "".join(
            self.codificar_letra(letra, desplazamiento) for letra in palabra
        )
        self.historial[palabra] = palabra_codificada
        return palabra_codificada

cc = CodificadorCesar()
resultado = cc.codificar_palabra("hola", 3)
print(resultado)
print(cc.historial)