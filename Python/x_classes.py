class Car:
    def __init__(self, manufacturer, model, color, engine, fuel, price, year):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.engine = engine
        self.fuel = fuel
        self.price = price
        self.year = year
        
    def print_info(self):
        print(self.manufacturer, self.model, self.color, self.engine, self.fuel, self.price, self.year)
    
    def __str__(self):
        return (f'Informações do Carro\nFabricante: {self.manufacturer}\nModelo: {self.model}\nCor: {self.color}\nMotor: {self.engine}\nCombustível: {self.fuel}\nPreço: €{self.price:,.2f}\nAno: {self.year}')

# Instância do Carro Seat Ibiza com preço em euros
ibiza = Car('Seat', 'Ibiza', 'Silver', '1.0', 'Gasoline', 14900, 2020)  # Preço ajustado para euros
print(ibiza)

class Extras(Car):
    def __init__(self, manufacturer, model, color, engine, fuel, price, year, air, airbags, alarm, gps):
        super().__init__(manufacturer, model, color, engine, fuel, price, year)
        self.air = air
        self.airbags = airbags
        self.alarm = alarm
        self.gps = gps
        
    def __str__(self):
        return (super().__str__() +
                f'\nExtras:\nAr Condicionado: {"Sim" if self.air else "Não"}\nAirbags: {"Sim" if self.airbags else "Não"}\nAlarme: {"Sim" if self.alarm else "Não"}\nGPS: {"Sim" if self.gps else "Não"}')

# Instância do carro BMW com extras e preço em euros
bmw = Extras('BMW', '320i', 'White', '2.0', 'Gasoline', 34000, 2022, True, True, True, True)
print(bmw)

class SUV(Extras):
    def __init__(self, manufacturer, model, color, engine, fuel, price, year, air, airbags, alarm, gps, four_x_four):
        super().__init__(manufacturer, model, color, engine, fuel, price, year, air, airbags, alarm, gps)
        self.four_x_four = four_x_four
        
    def __str__(self):
        return (super().__str__() +
                f'\nTração 4x4: {"Sim" if self.four_x_four else "Não"}')

# Instância do SUV Renault Captur com preço em euros
captur = SUV('Renault', 'Captur', 'Black', '1.3 Turbo', 'Gasoline', 25000, 2022, True, True, True, True, False)  
print(captur)
