# INSTRUCTIONS
# Create a function vowel_counting to loop through a string parameter and print to console how many vowels(“A”, “E”, “I”, “O”, “U” ) are in the argument. Save it in a module.

# Import the module you just saved. Call the function and pass your name as the argument.

# The output may look like this: 

    # My full name is Bing Li.

    # I have 2 vowels in my name.

def check_vowels(s):

    vowels = 'aeiouAEIOU'

    vowel_count = 0

    for char in s:

        if char in vowels:
            vowel_count += 1
            
    return vowel_count