import random

stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Game setup
placeholder = "_" * len(chosen_word)
lives = 6
game_over = False
guessed_letters = []

print("Welcome to Hangman!")

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        new_placeholder = ""
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                new_placeholder += guess
            else:
                new_placeholder += placeholder[i]
        placeholder = new_placeholder
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    print(stages[6 - lives])
    print("Word: ", placeholder)

    if "_" not in placeholder:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print("You lose!")
        print(f"The word was: {chosen_word}")