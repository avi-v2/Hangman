import random
from words import words
import string
def valid(w):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word

valid_guess=list(string.ascii_uppercase)
# print(valid_guess)
user=input("Enter your guess:\t").upper()
if user not in valid_guess:
     print("Invalid input: ")
