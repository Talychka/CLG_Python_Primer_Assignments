class Cat:
    number_of_eyes = 2

Cora = Cat()
Dora = Cat()
Nora = Cat()
Flora = Cat()

Flora.number_of_eyes = 1

print(Flora.number_of_eyes)


#     def __init__(self, name, breed):
#        self.name = name
#        self.breed = breed

# cat_1 = Cat('Hana', 'Ragdoll')
# cat_2 = Cat('Lulu', 'Taby')

# print(cat_1.number_of_eyes)
# print(cat_2.number_of_eyes)

# cat_1.number_of_eyes = 3

# print(cat_1.number_of_eyes)
# print(cat_2.number_of_eyes)

# print(cat_1.__dict__)
# print(Cat.__dict__)