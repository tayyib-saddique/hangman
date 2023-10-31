import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        '''Initalises variables for class

        Args: 
            word_list (list): list of words representing favourite fruit
            num_lives (int): number of lives for the game
        '''
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * ( len(self.word))
        self.num_letters = len(set(self.word))
        self.num_lives: int = num_lives
        self.word_list: list = word_list
        self.list_of_guesses: list = []

    def check_guess(self, guess: str):
        '''Processes character inputted by user. If user inputs character is found in word,
        character is appended to word_guessed list. Otherwise if character is not found in
        the word, the number of lives user has for game reduces by one.

        Args: 
            guess (str): single alphabetical character inputted by user
            
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            letter_indexes = []
            for index, letter in enumerate(self.word):
                if letter == guess:
                    letter_indexes.append(index)
            for index in letter_indexes:
                self.word_guessed[index] = guess
        else:
            print(f'Sorry, {guess} is not in the word. You have so far guessed:')
            for letter in self.list_of_guesses:
                if letter.isalpha() and len(guess) == 1:
                    print(f'{letter}', end = ' ')
            self.num_lives -= 1
            print(f'\nYou have {self.num_lives} lives left.')


    def ask_for_input(self):
        '''User is requested to provide input. If user provides invalid input, user is notified.
        Programme records previous history of inputs and calls check_guess function to review
        guess.
        '''
        while True:
            guess = input('Guess a letter.\n')
            if not guess.isalpha() and len(guess) == 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break
    

word_list = ['watermelon', 'mango', 'blackberry', 'strawberry', 'guava']
game = Hangman(word_list, 5)
game.ask_for_input()