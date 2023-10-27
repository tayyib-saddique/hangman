import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * ( len(self.word))
        self.num_letters = len(set(self.word))
        self.num_lives: int = num_lives
        self.word_list: list = word_list
        self.list_of_guesses: list = []

    def check_guess(self, guess: str):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            letter_index = self.word.index(guess)
            self.word_guessed[letter_index] = guess
        else:
            print(f'Sorry, {guess} is not in the word. You have so far guessed:')
            for letter in self.list_of_guesses:
                if letter.isalpha():
                    print(f'{letter}', end = ' ')
            self.num_lives -= 1
            print(f'\nYou have {self.num_lives} lives left.')


    def ask_for_input(self):
        while True:
            guess = input('Guess a letter. \n')
            if not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break



