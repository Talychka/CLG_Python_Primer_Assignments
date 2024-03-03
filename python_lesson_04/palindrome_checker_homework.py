#Palindrome checker
#Get input, convert to lower case, convert input (string) to a list
user_word = input("What is your favourite colour?").lower()
letters_in_word = list(user_word)
# create a reverse copy of the list in place using slicing
reversed_word_list=letters_in_word[::-1]
#check if it is a palindrome using boolean function
is_palindrome = letters_in_word == reversed_word_list
print(is_palindrome)
