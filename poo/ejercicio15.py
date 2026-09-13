#Clase RegistroNotas que: (1) tenga metodo registrar(estudiante, nota) que guarde en un diccionario;
# (2) tenga metodo estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; (3) tenga metodo mejor_estudiante()
#  que retorne nombre y nota del que tiene mayor calificación.
class RegistroNotas:
    def __init__(self):
        self.registros = {}

    def registrar(self, estudiante, nota):
        self.registros[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [
            estudiante for estudiante, nota in self.registros.items()
            if nota >= nota_minima
        ]

    def mejor_estudiante(self):
        if not self.registros:
            return None
        estudiante = max(self.registros, key=self.registros.get)
        return (estudiante, self.registros[estudiante])


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())
print(rn.estudiantes_aprobados(80))