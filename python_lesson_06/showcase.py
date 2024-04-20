about_me = {
    'name': 'Talya',
    'height': 1.76, 
    'hair colour': 'blonde', 
    'occupation': 'public servant', 
    'hobby': 'learning new languages'
}

for key, value in about_me.items():
    print(f'My {key} is {value}')

about_me['height'] = 1.75

about_me['favourite food'] = 'dahl'

about_me.pop('hair colour')

about_me_new = {'favourite colour': 'red', 'hobby': 'travelling'}
about_me.update(about_me_new)

print()
print("Hang on, I've had a bit of a rethink about that list, there were some mistakes and I forgot some things. Please forget about what I said before, what I actually want you to know about me is: ")
print()

for key, value in about_me.items():
    print(f'My {key} is {value}')

about_me.clear()

print()
print(f"Just joking, I was pulling your leg, none of that is true, my programmer made it all up. In fact, I am featureless, a ghost in the machine, an empty vessel. Here's a representation of everything there is to know about the real me: {about_me}")