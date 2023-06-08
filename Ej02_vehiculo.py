class Vehiculo:
    def __init__(self, color: str, ruedas: int) -> None:
        self.set_color(color)
        self.set_ruedas(ruedas)

    def get_color(self)-> str:
        print(f'El color de este vehículo es {self.color}')
    
    def get_ruedas(self)-> str:
        print(f'Este vehículo tiene {self.ruedas} ruedas.')

    def set_color(self, color)-> None:
        self.color = color
    
    def set_ruedas(self, ruedas)-> None:
        self.ruedas = ruedas

    prop_color = property(get_color, set_color)
    prop_ruedas = property(get_ruedas, set_ruedas)


class Coche(Vehiculo):
    def __init__(self, color: str, ruedas: int, velocidad: int, cilindrada: int) -> None:
        super().__init__(color, ruedas)
        self.set_velocidad(velocidad)
        self.set_cilindrada(cilindrada)

    def get_velocidad(self)-> str:
        print(f'Este coche alcanza una velocidad de {self.velocidad} Km/h.')
  
    def get_cilindrada(self)-> str:
        print(f'Este coche tiene una cilindrada de {self.cilindrada} cc.')

    def set_velocidad(self, velocidad)-> None:
        self.velocidad = velocidad
  
    def set_cilindrada(self, cilindrada)-> None:
        self.cilindrada = cilindrada

    prop_velocidad = property(get_velocidad, set_velocidad)
    prop_cilindrada = property(get_cilindrada, set_cilindrada)


class Camioneta(Coche):
    def __init__(self, color: str, ruedas: int, velocidad: int, cilindrada: int, carga: int) -> None:
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.set_carga(carga)

    def get_carga(self)-> str:
        print(f'Este camioneta puede cargar {self.carga} Kg.')
  
    def set_carga(self, carga)-> None:
        self.carga = carga

    prop_carga = property(get_carga, set_carga)


class Bicicleta(Vehiculo):
    '''El tipo puede ser "urbana" o "deportiva" '''
    def __init__(self, color: str, ruedas: int, tipo: str) -> None:
        super().__init__(color, ruedas)
        self.set_tipo(tipo)

    def get_tipo(self)-> str:
        print(f'Esta bicicleta es del tipo {self.tipo}.')
  
    def set_tipo(self, tipo)-> None:
        if tipo in ('urbana', 'deportiva'):
            self.tipo = tipo
        else:
            print('Los valores aceptados son "urbana" o "deportiva"')

    prop_tipo = property(get_tipo, set_tipo)


class Motocicleta(Bicicleta):
    '''El tipo puede ser "urbana" o "deportiva" '''
    def __init__(self, color: str, ruedas: int, tipo: str, velocidad: int, cilindrada: int) -> None:
        super().__init__(color, ruedas, tipo)
        self.set_velocidad(velocidad)
        self.set_cilindrada(cilindrada)

    def get_velocidad(self)-> str:
        print(f'Esta motocicleta alcanza una velocidad de {self.velocidad} Km/h.')
  
    def get_cilindrada(self)-> str:
        print(f'Esta motocicleta tiene una cilindrada de {self.cilindrada} cc.')

    def set_velocidad(self, velocidad)-> None:
        self.velocidad = velocidad
  
    def set_cilindrada(self, cilindrada)-> None:
        self.cilindrada = cilindrada

    prop_velocidad = property(get_velocidad, set_velocidad)
    prop_cilindrada = property(get_cilindrada, set_cilindrada)
