
#CLASE EDIFICIOS

class Edificio:

    #Atributos del Objeto

    def __init__(self,type,huella,dptos,ancho,largo,adpto,prior):

        self.type = type
        self.huella = huella
        self.dptos = dptos
        self.ancho = ancho
        self.largo = largo
        self.adpto = adpto
        self.prior = prior

    # Metodos del Objeto

    def num_max_vivedif (self,num_vivmax):
        return round((self.prior*num_vivmax)/100)
    def viv_init (self):
        return self.dptos
    def niv_tedif (self,num_vivmax):
        return round(((self.prior*num_vivmax)/100) / self.dptos)


