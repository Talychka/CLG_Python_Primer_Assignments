money_start = input("How much money did you put into your term deposit? (Please enter whole numbers only, without commas or cents) $ ")
saving_years = input("How many years duration is your term deposit? (Please enter whole numbers only) ")
interest_rate = input("What is the interest rate on your term deposit? (Please include decimal points) % ")
money_result = int(money_start) + (int(money_start) * int(saving_years)* (float(interest_rate)/100))
print(f"When your term deposit expires you will have ${money_result:.2f}.")
print(f"Will you be able to afford your holiday?")
if money_result >= 10000:
    print(f"Yes! Have an amazing time and send us a postcard!")
else:
    print(f"Unfortunately, that won't quite get you your dream holiday. Can you put down a bigger deposit, extend the term of your savings or find a better interest rate?")