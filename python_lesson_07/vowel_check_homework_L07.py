import vowel_checker_module
user_name = input("Please write your full name here. Don't forget your middle name(s)!: ")
vowel_count = vowel_checker_module.check_vowels(user_name)
print(f"Your name is {user_name}. There are {vowel_count} vowel(es) in your name.")