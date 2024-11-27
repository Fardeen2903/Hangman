import random
import nltk
from nltk.corpus import wordnet as wn
from collections import Counter

# Download necessary nltk data
nltk.download('words')
nltk.download('wordnet')

# Load the list of English words from NLTK
word_list = nltk.corpus.words.words()

# Function to fetch the definition of a word
def get_word_definition(word):
    synsets = wn.synsets(word)
    if synsets:
        return synsets[0].definition()
    return "No definition available"

# Function to draw the hangman based on mistakes
def draw_hangman(mistakes):
    hangman_graphics = [
        '''
         ------
         |    |
              |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
         |    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
              |
        =========
        '''
    ]
    print(hangman_graphics[mistakes])

# Randomly choose a secret word from the English dictionary
word = random.choice(word_list)
word_definition = get_word_definition(word)

if __name__ == '__main__':
    print('Guess the word! HINT: ' + word_definition)

    # Display empty spaces for the word
    for _ in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    mistakes = 0
    chances = 6  # Allow 6 mistakes
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            print(f"Remaining chances: {chances - mistakes}")
            draw_hangman(mistakes)

            try:
                guess = input('Enter a letter to guess: ').lower()
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # Add guessed letter as many times as it occurs

            # Print the word with guessed letters
            correct = 0
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                    correct += 1
                else:
                    print('_', end=' ')

            # Check if the word is completely guessed
            if Counter(letterGuessed) == Counter(word):
                print(f"\nThe word is: {word}")
                print('Congratulations, You won!')
                flag = 1
                break

            # If guessed letter is wrong
            if guess not in word:
                mistakes += 1

            # If the player used all their chances
            if mistakes >= chances:
                print()
                print(f"You lost! The word was '{word}'")
                break

    except KeyboardInterrupt:
        print("\nBye! Try again.")
        exit()
