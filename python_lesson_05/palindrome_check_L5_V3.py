#define variable using input
user_phrase = input("Please enter a three or four word phrase using only alphabetic characters: ")

# Replace spaces with hyphens
modified_phrase = user_phrase.replace(' ', '')

# Keep looping until all elements are strings
while not modified_phrase.isalpha():
    user_phrase = input("Invalid input. Please enter a phrase using only alphabetic characters: ")
    modified_phrase = user_phrase.replace(' ', '')
    if modified_phrase.isalpha():  # If all elements are strings and alphabetic, break the loop
        break

#check if it is a palindrome using boolean function
if modified_phrase.lower() == modified_phrase.lower()[::-1]:
    print("How unusual, this phrase is a Palindrome!")
else:
    print("Unsurprisingly, this phrase is not a Palindrome")