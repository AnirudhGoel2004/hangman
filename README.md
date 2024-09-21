# Hangman Game

A simple Python implementation of the classic word-guessing game **Hangman**. The player must guess a secret word letter by letter within a limited number of incorrect guesses. This version of the game loads the words from an external file called `words.txt`.

## How to Play

- The computer randomly selects a word from the `words.txt` file.
- The player guesses one letter at a time.
- For each incorrect guess, part of a hangman figure is drawn.
- The player wins if they guess the entire word before the hangman is fully drawn.
- The player loses if the hangman is fully drawn before the word is guessed.

## Features

- Reads words from an external `words.txt` file.
- Visual representation of the hangman’s state with each incorrect guess.
