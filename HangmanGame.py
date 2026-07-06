import random
words = ["apple", "mango", "tiger", "table", "school"]

word = random.choice(words)

guessed = ["_"] * len(word)

wrong_guesses = 0
max_wrong = 6
guessed_letters = []

print("===== HANGMAN GAME =====")

while wrong_guesses < max_wrong and "_" in guessed:

    print("\nWord:", " ".join(guessed))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    letter = input("Enter a letter: ").lower()

    if letter in guessed_letters:
        print("You already guessed that letter!")
    else:
        guessed_letters.append(letter)
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Wrong!")

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)
