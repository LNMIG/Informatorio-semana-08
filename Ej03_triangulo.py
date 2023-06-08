class Triangulo:
    def __init__(self, lado1: float, lado2: float, lado3: float)-> None:
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
    
    def get_lado_mayor(self)-> str:
        print(f'El lado mayor del triángulo mide {max(self.__lado1, self.__lado2, self.__lado3)}')
    
    def get_tipo_triangulo(self)-> str:
        self.tipo = ''
        if self.__lado1 == self.__lado2 == self.__lado3:
            self.tipo = 'Equilatero'
        elif self.__lado1 == self.__lado2 or self.__lado1 == self.__lado3 or self.__lado2 == self.__lado3:
            self.tipo = 'Isosceles'
        else:
            self.tipo = 'Escaleno'
        print(f'El tipo de triángulo ingresado es {self.tipo}.')