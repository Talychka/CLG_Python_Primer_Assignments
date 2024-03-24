def get_average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    mean = total/len(numbers)

    return mean
ratings = [5,5,4]
average = get_average(ratings)
print(average)

def greet_new(name, is_new):
    if is_new == True:
        print(f'Hi, {name}! Welcome to Code Like a Girl!')
    else:
        print(f'Hi {name}! Welcome back!')
greet_new('Raj', True)
greet_new('Chloe', False)

def greet_new_default(name, is_new=True):
    if is_new == True:
        print(f'Hi, {name}! Welcome to Code Like a Girl!')
    else:  
        print(f'Hi, {name}! Welcome back!')

greet_new_default('April')
greet_new_default('Katerina', False)
greet_new_default(is_new=False, name='Amy')

def build_person(first_name, last_name, age=''):
    person={'first': first_name, 'last': last_name}
    if age:
        person['age']=age
    return person

patient_0 = build_person('Angela', 'Tran')
print(patient_0)
patient_1= build_person('Ricky', 'Lim', 39)
print(patient_1)

