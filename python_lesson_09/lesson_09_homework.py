class KitchenAppliance:

    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    
    def report(self):
        print("This is machine number " + str(self.model_number) + ". I am the " + self.brand + " model.")

class SmartCoffeeMachine(KitchenAppliance):

    def __init__(self, model_number, brand, coffee_menu={'cafe latte', 'cappuccino', 'flat white', 'macchiato'}):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = set(coffee_menu)
        
    def make_coffee(self, coffee_menu):
        while True:
            coffee_order = input(f"Here is a list of the currently available coffee types in our menu: {self.coffee_menu}. Please tell me which type of coffee you would like to drink: ")

            if coffee_order in self.coffee_menu: 
                print("Great, that's available, I'll get right on it!")
                break
            else:
                input(f"Unfortunately that type of coffee is currently unavailable. Here is today's menu: {self.coffee_menu}. Please tell me which type of coffee you would like to drink: ")
          

    def update_menu(self, new_coffee):
        new_coffee = input("I'm sorry if you were unable to order your preferred coffee today. Please tell us the new type of coffee you would love us to add to the menu: ")
        self.coffee_menu.add(new_coffee)
        print(f'''Thanks for your feedback and for continuing to be one of our favourite customers! 
              We always love to hear new ideas and will add your coffee suggestion to our menu.
              From next Tuesday you'll be able to order any of the following coffees from our menu: {self.coffee_menu}''')
        return self.coffee_menu

my_coffee_machine = SmartCoffeeMachine(123, 'Snazzy Caff')
my_coffee_machine.report()
print(my_coffee_machine.coffee_menu)
my_coffee_machine.make_coffee({})
my_coffee_machine.update_menu({})
print(my_coffee_machine.coffee_menu)