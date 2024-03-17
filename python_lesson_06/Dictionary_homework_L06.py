# Create a variable with your name.

# Assign a dictionary to the variable with your information (age, occupation, hobby, etc).

# Use for loop to iterate through the dictionary and F-string to print each key value pair (eg. “My favourite color is green.”)

# Try add, delete, update and clear data from your dictionary.

# Create a dictionary
about_me = {'name': 'Talya', 'age': 48, 'height': 1.76, 'hair colour': 'blonde', 'occupation': 'public servant', 'hobby': 'learning new languages'}

# Run a for loop to iterate through the dictionary and print it out
for key, value in about_me.items():
    print(f'My {key} is {value}')

#change a value
about_me['height'] = 1.75

# Add a key-value pair
about_me['favourite food'] = 'dahl'

# Delete a key-value pair
about_me.pop('age')

# Update the dictionary
about_me_new = {'favourite colour': 'red', 'hobby': 'travelling'}
about_me.update(about_me_new)

print()
print("Hang on, I've had a bit of a rethink about that list, there were some mistakes and I forgot some things. Please forget about what I said before, what I actually want you to know about me is: ")
print()

for key, value in about_me.items():
    print(f'My {key} is {value}')

# clear the dictionary

about_me.clear()

print()
print(f"Just joking, I was pulling your leg, none of that is true, my programmer made it all up. In fact, I am featureless, a ghost in the machine, an empty vessel. Here's a representation of everything there is to know about the real me: {about_me}")
