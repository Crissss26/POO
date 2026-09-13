#Clase AnalizadorString que: (1) tenga metodo solo_vocales(letra) que retorne True si es vocal;
# (2) tenga metodo contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando metodos;
#  (3) tenga atributo que guarde el texto maás largo analizado.
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiouáéíóú"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteos = {'vocales': 0, 'consonantes': 0, 'digitos': 0}

        for caracter in texto:
            if caracter.isdigit():
                conteos['digitos'] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    conteos['vocales'] += 1
                else:
                    conteos['consonantes'] += 1

        return conteos

astr = AnalizadorString()
resultado = astr.contar_por_tipo("Hola123")
print(resultado)
astr.contar_por_tipo("Programación Python")
print(astr.texto_mas_largo)