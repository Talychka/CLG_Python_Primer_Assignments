#define variable using input
user_phrase = input("Please enter a three or four word phrase using only alphabetic characters: ")

# Replace spaces with hyphens
modified_phrase = user_phrase.replace(' ', '')

# Convert elements to a list
phrase_list = list(modified_phrase)

# Keep looping until all elements are strings
while not phrase_list.isalpha():
    user_phrase = input("Invalid input. Please enter a phrase using only alphabetic characters: ")
    modified_phrase = user_phrase.replace(' ', '')
    phrase_list = list(modified_phrase)
    if phrase_list.isalpha():  # If all elements are strings and alphabetic, break the loop
        break

#check if it is a palindrome using boolean function
if phrase_list.lower() == phrase_list.lower()[::-1]:
    print("How unusual, this phrase is a Palindrome!")
else:
    print("Unsurprisingly, this phrase is not a Palindrome")