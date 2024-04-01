class AirConditioner:
    def __init__(self, model_number, brand, price):
        self.model_number = model_number
        self.brand = brand
        self.price = price
    
    def cooling(self):
        print("It's cooling.")

    def heating(self):
        print("It's heating.")

    def report(self, temperature):
        print(f"""Hi! This is your {self.brand} air conditioner. 
              The current temperature outside is {str(temperature)} degrees Celsius.""")

aircon_0 = AirConditioner(12345, 'Mitsubishi', 2299.99)
aircon_1 = AirConditioner(12346, 'Daikin', 2999.49)
aircon_3 = AirConditioner(12347, 'Fujitsu', 1899.50)

print("The model number of aircon_0 is " + str(aircon_0.model_number))
print("The brand of aircon_0 is " + aircon_0.brand)
print("The price of aircon_0 is $" + str(aircon_0.price) + '.')

aircon_0.cooling()
aircon_0.heating()
aircon_0.report(13)

