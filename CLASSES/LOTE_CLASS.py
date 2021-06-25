# CLASE LOTES
class Lote:

    #Atributos Objeto

    def __init__(self,nombre,uso_suelo,max_viv,max_niv,altura_max,superficie,cos,a_libre,a_verde):

        self.nombre = nombre
        self.uso_suelo = uso_suelo
        self.max_viv = max_viv
        self.max_niv = max_niv
        self.altura_max = altura_max
        self.superficie = superficie
        self.cos = cos
        self.a_libre = a_libre
        self.a_verde = a_verde

    # Metodos del Objeto:

    def lim_maxcos (self):
        return self.superficie * self.cos
    def lim_maxalibre (self):
        return self.superficie * self.a_libre
    def lim_maxaverde (self):
        return self.superficie * self.a_verde
    def areamax_cons (self):
        return (self.superficie * self.max_niv) /2
    def cus (self):
        cus = (self.superficie*self.cos) * self.max_niv
        return (cus / self.superficie) * (self.superficie * self.max_niv) /2




























































lote01 = Lote("Lote 01","c.u",117,15,75,14611.43,0.50,0.25,0.25)

print(lote01.lim_maxcos())
print(lote01.lim_maxalibre())
print(lote01.lim_maxaverde())
print(lote01.areamax_cons())
print(lote01.cus())

