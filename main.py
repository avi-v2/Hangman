import random
from words import words 
import string

def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

valid_letters = string.ascii_uppercase
word = get_valid_word()
guessed_letters = []
answer = ["_" for i in word]

print("Welcome to the Word Guessing Game!")

while True:
    print("\nCurrent word: ", " ".join(answer))
    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))

    user_input = input("Enter your guess: ").upper()

    if len(user_input) != 1 or user_input not in valid_letters:
        print("❌ Invalid input. Please enter a single letter (A-Z).")
        continue

    if user_input in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(user_input)

    if user_input in word:
        print("✅ Good guess!")
        for idx, char in enumerate(word):
            if char == user_input:
                answer[idx] = char
    else:
        print("❌ That letter is not in the word.")

    if "_" not in answer:
        print("\n🎉 Congratulations! You've guessed the word:", word)
        break
