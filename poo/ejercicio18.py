#Clase AgrupadorEdades que: (1) tenga metodo clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor");
# (2) tenga m3todo agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; (3) tenga metodo edad_promedio_categoria(categoria).
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {
            'niño': [],
            'adolescente': [],
            'adulto': [],
            'mayor': []
        }

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {'niño': [], 'adolescente': [], 'adulto': [], 'mayor': []}

        for edad in edades:
            cat = self.clasificar_edad(edad)
            self.grupos[cat].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        lista_edades = self.grupos.get(categoria, [])
        if not lista_edades:
            return 0
        return sum(lista_edades) / len(lista_edades)


ae = AgrupadorEdades()
resultado = ae.agrupar_por_categoria(5, 15, 30, 70)
print(resultado)
print(ae.edad_promedio_categoria("adulto"))