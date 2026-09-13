#Clase Tareas que: (1) tenga metodo agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad);
# (2) tenga metodo tareas_prioritarias() que retorne solo las de prioridad alta; (3) tenga metodo eliminar_completada(descripcion)
#  que borre la tarea de la lista.

class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [
            tarea for tarea in self.lista_tareas
            if tarea[1].lower() == "alta"
        ]

    def eliminar_completada(self, descripcion):
        self.lista_tareas = [
            tarea for tarea in self.lista_tareas
            if tarea[0] != descripcion
        ]

t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())
t.eliminar_completada("Leer")
print(t.lista_tareas)