import random
from words import words
import string
def valid():
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=(random.choice(words))
    return list(word.upper())

valid_guess=(string.ascii_uppercase)
# print(valid_guess)
word=(valid())

ans=[]
for i in word:
    ans.append("_")
print(word)
guessed=[]
while True:
    print(f"The word is {ans}")
    user=input("Enter your guess:\t").upper()
    if len(guessed)>0:
        print("guessed words:", guessed)
    if user not in valid_guess:
        print("Invalid input: ")
    if user not in guessed:
        guessed.append(user)
    else:
        print("Letter already guessed")
    for i,l in enumerate(word):
        if l==user:
            ans[i]=l
    if "_" not in ans:
        print("You Won")
        print("The word was ", word)