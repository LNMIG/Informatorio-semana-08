from Ej02_vehiculo import Coche, Camioneta, Bicicleta, Motocicleta


# -- Probando la subclase Coche --
coche1 = Coche('rojo', 4, 180, 1800)
camioneta1 = Camioneta('gris', 4, 180, 2100, 900)
bicicleta1 = Bicicleta('verde', 2,'urbana')
motocicleta1 = Motocicleta('azul', 2, 'deportiva', 100, 600)

vehiculos = [coche1, camioneta1, bicicleta1, motocicleta1]


# def catalogar(vehiculos):
#     for each in vehiculos:
#         print(f'El nombre de la clase del objeto es "{type(each).__name__}" y sus atributos son {list(each.__dict__)}\n')

# catalogar(vehiculos)

def catalogar(vehiculos, ruedas=None):
    contador_ruedas = 0
    for each in vehiculos:
        if ruedas > 0:
            if ruedas == each.ruedas:
                print(f'El nombre de la clase del objeto es "{type(each).__name__}" y sus atributos son {list(each.__dict__)}\n')
                contador_ruedas += 1
            else:
              continue
    if ruedas > 0:
        print(f'Se han encontrado {contador_ruedas} vehículos con {ruedas} ruedas.')
    else:
        print(f'No se encontraron vehículosSe con {ruedas} ruedas.')

catalogar(vehiculos, 0)