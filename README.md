# Hangman
simple hangman game in python

## Description

This is a Python implementation of the classic **Hangman game**. In this version, the game randomly selects a word from the English dictionary and provides a hint by displaying its definition. The player must guess the word by suggesting letters. With each incorrect guess, an ASCII representation of a hangman is drawn. The player is allowed a maximum of 6 incorrect guesses before losing the game.

### Features:
- Randomly selects a word from the English dictionary.
- Provides a definition of the word as a hint.
- ASCII art for the hangman, which progresses with each mistake.
- A total of 6 allowed mistakes before the game ends.

## Requirements

- Python 3.x
- `nltk` library for word selection and definitions

### Install the required libraries:
To run the game, you'll need to install the following Python libraries:

```bash
pip install nltk
```

### Download necessary NLTK data:
The `nltk` library requires downloading certain corpora. You can do this by running the following commands:

```python
import nltk
nltk.download('words')
nltk.download('wordnet')
```

## How to Play

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Fardeen2903/hangman-game.git
   ```
2. Navigate into the project directory:
   ```bash
   cd hangman-game
   ```
3. Run the Python script to start the game:
   ```bash
   python hangman.py
   ```

4. Follow the on-screen prompts to guess the word. Enter one letter at a time. If you guess incorrectly, the hangman will progressively be drawn.

5. The game ends when you either guess the word correctly or use up all your allowed incorrect guesses.

## License

This project is licensed under the **BSD 2-Clause License** - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **[nltk](https://www.nltk.org/)**: Used for fetching the list of English words and definitions from WordNet.
- **ASCII Hangman Graphics**: Custom ASCII art for the hangman drawing.

## Contact

Feel free to open an issue or submit a pull request if you have suggestions or improvements!

---
