# def is_palindrome(word):
#     word = input().lower()
#     letters_in_word = list(word)
#     reversed_word=letters_in_word[::-1]
#     is_palindrome = letters_in_word == reversed_word
#     return(is_palindrome)

#     def is_palindrome(self, word):
#         word = word.lower()
#         return word == word[::-1]
    
def is_palindrome(word):
    word = word.lower()
    letters_in_word = list(word)
    reversed_word=letters_in_word[::-1]
    is_palindrome = letters_in_word == reversed_word
    return(is_palindrome)

    
    def is_palindrome(self, user_password):
        user_password = user_password.lower()
        letters_in_word = list(user_password)
        reversed_word=letters_in_word[::-1]
        is_palindrome = letters_in_word == reversed_word
        return(is_palindrome)