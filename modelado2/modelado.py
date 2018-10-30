class Materia(object):
    def __init__(self):
        self.codigo = ""
        self.nombre = ""

    def presentar_datos(self):
        return "%s-%s" % (self.obtener_codigo(), self.nombre)

    def agregar_codigo(self, c):  
        self.codigo = c

    def obtener_codigo(self):
        return self.codigo

    def agregar_nombre(self, n):  
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    


class MateriaPresencial(Materia):
    def __init__(self):

        super(MateriaPresencial, self).__init__()
        self.num_creditos = 0

    def agregar_num_creditos(self, a):  
        self.num_creditos = a

    def obtener_num_creditos(self):
        return self.num_creditos

    def presentar_datos(self):
        return "%s-%s" % (super(MateriaPresencial, self).presentar_datos(), self.num_creditos)