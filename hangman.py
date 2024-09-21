import random

# Function to load words from a file
def load_words(file_path):
    """Load words from a text file and return a list of words."""
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []

def get_word(word_list):
    """Randomly selects a word from the word list."""
    return random.choice(word_list)

def display_hangman(tries):
    """Displays the current state of the hangman depending on the number of incorrect tries."""
    stages = [
        """
           --------
           |      |
           |      
           |    
           |     
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |    
           |     
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |     
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |     
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]
    return stages[tries]

def play_hangman():
    word_list = load_words("words.txt")  # Load words from the file
    if not word_list:
        return  # Exit if no words are loaded

    word = get_word(word_list)
    word_letters = set(word)  # The unique letters in the word
    guessed_letters = set()  # Letters guessed by the player
    tries = 0  # Number of incorrect guesses
    max_tries = 6  # Maximum number of incorrect guesses

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))

    while tries < max_tries and word_letters:
        guess = input("\nGuess a letter: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            tries += 1
            guessed_letters.add(guess)
            print(f"Wrong guess! {guess} is not in the word.")

        # Display the current state of the game
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(display_hangman(tries))
        print(" ".join(word_display))

    # Check if the player has won or lost
    if not word_letters:
        print(f"Congratulations! You've guessed the word '{word}'!")
    else:
        print(f"Sorry, you've run out of tries. The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
