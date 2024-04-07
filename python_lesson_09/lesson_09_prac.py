# class ParentClass:

#     def __init__(self):
#         pass

# class ChildClass(ParentClass):
#     pass

# class Pet:
#     def __init__(self, breed):
#         self.breed = breed

# class Cat(Pet):
#     def meow(self):
#              print('Meow!')

# paws = Cat('Ragdoll')
# print(paws.breed)
# paws.meow()

# class SmartDevice:
#     def __init__(self, model_number, brand, screen_size, app_list = []):
#         self.model_number = model_number
#         self.brand = brand
#         self.screen_size = screen_size
#         self.app_list = app_list

#     def report(self):
#         print(f"This is " + str(self.model_number) + " from " + self.brand)

#     def install_app(self, app_name = "Demo app"):
#         print(f"Installing {app_name}...")
#         self.app_list.append(app_name)
#         return self.app_list

# class Phone(SmartDevice):
#     def __init__(self, model_number, brand, screen_size, app_list = [], os='iOS'):
#         SmartDevice.__init__(self, model_number, brand,
#                              screen_size, app_list)
#         self.os = os

#     def call(self, phone_number):
#         print('Calling...' + phone_number)

# phone_b = Phone(243455, 'Apple', 4.3)
# phone_b.install_app('Animal Crossing')
# phone_b.call('0412345678')
# print(phone_b.app_list)

# class SmartDevice:
#     def __init__(self, model):
#         self.model = model
#         self._os_version = "4.2.1"
#         self._check_os_version()

#     def _check_os_version(self):
#         print(f"Running operating system {self._os_version}")

# class Phone(SmartDevice):
#     def __init__(self, model, screen_size):
#         SmartDevice.__init__(self, model)
#         self.screen_size = screen_size
#         self._os_version = "5.0.1"
#         self._check_os_version()

# device = SmartDevice("Z-1385")
# device._os_version = "10.0"
# phone = Phone("iPhone 12", "Max")

# class HardDisk:
#     def __init__(self, operating_system, size):
#         self.operating_system = operating_system
#         self.size = size
#         self.__password = 'pAs5c0d3'

#     def __create_backup(self):
#         print("Backup created.")

# disk = HardDisk("Windows", "1TB")

# disk._HardDisk__create_backup()
# # # print(disk.__dict__)
# # print(disk._HardDisk__password)

# print(1+1)
# print(0.42 + 2.33)
# print('Hello' + ' human!')
# print(['red', 'green'] + ['yellow'])

# class Pet:
#     def __init__(self, breed):
#         self.breed = breed

# class Dog(Pet):
#     def __init__(self, breed):
#         Pet.__init__(self, breed)
    
#     def greet_human(self, name):
#         print("Welcome home, " + name + "!")

# class Cat(Pet):
#     def __init__(self, breed):
#         Pet.__init__(self, breed)

#     def greet_human(self, name):
#         print(name + ", come and serve me!")

# pets = [Dog('Shiba'), Cat('British Shorthair')]

# pets[0].greet_human('Melody')
# pets[1].greet_human('Asuka')

# class Pet:
#     def __init__(self, breed):
#         self.breed = breed

#     def greet_human(self, name):
#         print("Hello " + name + "!")

# class Dog(Pet):
#     def __init__(self, breed):
#         Pet.__init__(self, breed)

# class Cat(Pet):
#     def __init__(self, breed):
#         Pet.__init__(self, breed)

#     def greet_human(self, name):
#         print(name + ", come and serve me!")

# pets = [Dog('Shiba'), Cat('British Shorthair')]

# pets[0].greet_human('Melody')
# pets[1].greet_human('Asuka')


# class Dog:
#     def __init__(self, breed):
#         self.breed = breed

#     def greet_human(self, name):
#         print("Welcome home, " + name + "!")

# class Cat:
#     def __init__(self, breed):
#         self.breed = breed
    
#     def greet_human(self, name):
#         print(name + ", come and serve me!")

# def greet(animal):
#     animal.greet_human('Alisa')

# dog = Dog('Pug')
# cat = Cat('Russian Blue')

# greet(dog)
# greet(cat)

# print(len('Code like a girl'))
# print(len(['Python', 'C#', 'Javascript']))
# print(len({'name': 'Emma', 'breed': 'Husky'}))

# class Movie:
#     def __init__(self, name, running_time):
#         self.name = name
#         self.running_time = running_time

#     def __len__(self):
#         return int(self.running_time)

# movie = Movie('The Matrix', 136.4)
# print(len(movie))

class Coffee:
    def consume(self):
        print("Now I'm ready to work!")

class Cake:
    def consume(self):
        print("Now I'm ready to sleep...")

menu_items = (Coffee(), Cake())
for item  in menu_items:
    item.consume()


