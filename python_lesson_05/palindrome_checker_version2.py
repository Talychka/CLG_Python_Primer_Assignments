#Palindrome checker version 2

#Initialize the variable with user input
user_phrase = input("Please enter a three or four word phrase using alphabetic characters only: ")

#Convert elements to a list
phrase_list = list(user_phrase)

#Keep looping until all elements are strings
while False (all(isinstance(item, str) for item in phrase_list)):
    user_phrase = input("Please enter a three or four word phrase using alphabetic characters only: ")
    
    if True (all(isinstance(item, str) for item in phrase_list)):
        break

#Convert to lowercase
clean_phrase = [char.lower() for char in phrase_list if char.isalpha()]

# create a reverse copy of the list in place using slicing
reversed_phrase_list=clean_phrase[::-1]

#check if it is a palindrome using boolean function
if clean_phrase == reversed_phrase_list:
    print("This phrase is a Palindrome")
else:
    print("This phrase is not a Palindrome")
