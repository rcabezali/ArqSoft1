class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando...")

    def detener(self):
        print(f"El {self.marca} {self.modelo} se ha detenido.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def tocar_bocina(self):
        print(f"El coche {self.marca} {self.modelo} dice: ¡Beep beep!")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def hacer_caballito(self):
        print(f"La moto {self.marca} {self.modelo} está haciendo un caballito.")

# Función principal
def main():
    vehiculos = [
        Coche("Toyota", "Corolla", 2020, 4),
        Moto("Yamaha", "R1", 2019, "deportiva"),
        Coche("Ford", "Fiesta", 2021, 5),
        Moto("Honda", "PCX", 2022, "scooter")
    ]

    for vehiculo in vehiculos:
        vehiculo.arrancar()
        if isinstance(vehiculo, Coche):
            vehiculo.tocar_bocina()
        elif isinstance(vehiculo, Moto):
            vehiculo.hacer_caballito()
        vehiculo.detener()

if __name__ == "__main__":
    main()
