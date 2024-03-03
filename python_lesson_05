#define variable using input
user_phrase = input("Please enter a three or four word phrase using only alphabetic characters: ")

# Replace spaces with hyphens
modified_phrase = user_phrase.replace(' ', '')

# Convert elements to a list
phrase_list = list(modified_phrase)

# Keep looping until all elements are strings
while False (all(char.isalpha() for char in phrase_list)):
    user_phrase = input("Invalid input. Please enter a phrase using only alphabetic characters: ")
    if True (all(char.isalpha() for char in phrase_list)):  # If all elements are strings and alphabetic, break the loop
        break
 
# Convert to lowercase
clean_phrase = [char.lower() for char in phrase_list]

# create a reverse copy of the list in place using slicing
reversed_phrase_list=clean_phrase[::-1]

#check if it is a palindrome using boolean function
if clean_phrase == reversed_phrase_list:
    print("This phrase is a Palindrome")
else:
    print("This phrase is not a Palindrome")