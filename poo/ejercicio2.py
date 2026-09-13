#Clase Calificador que: (1) tenga metodo validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario;
#(2) tenga metodo cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna,
#y retorne esa lista; (3) tenga metodo promedio() que retorne el promedio de notas almacenadas.
class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())