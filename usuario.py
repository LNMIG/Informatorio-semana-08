class Usuario:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def setNamePassword(self, name, password):
        self.name = name
        self.password = password
    
    def getNamePassword(self):
        print(f'El nombre es: {self.name} y la contraseña es: {self.password}.')
        return
