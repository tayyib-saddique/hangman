import random

word_list = ['watermelon', 'mango', 'blackberry', 'strawberry', 'guava']

word = random.choice(word_list)
print(word)

guess = input('Enter a single letter \n')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
