import random

# List of 5 predefined words
words = ["python", "program", "code_alpha", "coding", "college"]

# Choose a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Game loop
while incorrect_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses:", incorrect_guesses)

    # Take input
    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:

        print("Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check the result
if "_" not in guessed_word:
    print("\nCongratulations! You won!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)