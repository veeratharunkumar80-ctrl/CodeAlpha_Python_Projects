import random

words = ["python", "apple", "computer", "programming", "internship"]

word = random.choice(words)
guessed = ["_"] * len(word)

attempts = 6

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed:
    print("\nCongratulations! The word was:", word)
else:
    print("\nGame Over! The word was:", word)