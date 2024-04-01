class RiceCooker:
    def __init__(self, model_number, price):
        self.model_number = model_number
        self.price = price
    def cook_rice(self):
        print("The rice is cooked inside.")

    def keep_warm(self):
        print("Rice is warm.")

    def greet(self, name):
        print(f"Hi {name}, this is rice cooker number {self.model_number} and it costs ${self.price}")

rice_cooker_0 = RiceCooker(27654, 249.99)

print(rice_cooker_0.model_number)
print(rice_cooker_0.price)

rice_cooker_0.cook_rice()
rice_cooker_0.keep_warm()

rice_cooker_1 = RiceCooker(27655, 279.99)
rice_cooker_1.greet('Talya')

rice_cooker_0.greet('Talya')

    