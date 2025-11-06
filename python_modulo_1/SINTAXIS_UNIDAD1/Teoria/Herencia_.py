class vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
        
    def encender(self):
        self.encendido = True
        return f"{self.marca} {self.modelo} encendido"
    
    def apagar(self):
        self.encendido = False
        return f"{self.marca} {self.modelo} apagado"
    
    def describir(self):
        return f"Vehículo: {self.marca} {self.modelo} del año {self.año}"
    
    
class Automovil(vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        vehiculo.__init__(self, marca, modelo, año)
        self.puertas = puertas
        
    def describir(self):
        return f"Automóvil: {self.marca} {self.modelo} del año {self.año} con {self.puertas} puertas."
    
mi_auto = Automovil("toyota", "Corolla", 2023, 4)


        
        

