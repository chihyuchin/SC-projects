"""
File: hangman.py
ChihYu Chin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    players are asked to type a alphabet at each round to guess the vocabulary
    players have 7 chances to make mistakes
    illegal format does not count as mistakes
    """

    word = random_word()
    line = ('-' * len(word))   # this is to show players how many alphabets the word has
    count = 0
    life = N_TURNS
    print('The word looks like: ' + line)
    print('You have ' + str(life) + ' guesses left.')
    while True:
        guess = str(input('Your guess: '))
        """
        Below lines are to inform players that they key in the wrong format
        """
        if guess.isalpha() == False:
            print('Illegal format')
        elif len(guess) > 1:
            print('Illegal format')
        else:
            guess = guess.upper()  # To make sure its case insensitive
            for i in range(len(word)):
                if word[i].find(guess) != -1:  # this is when players guess the right alphabet
                    """
                    Below lines are to show the right alphabet players guess to replace the '-'
                    Devide the new line into three part, first part, last part and the right guessing part
                    """
                    count += 1
                    first = line[:i]
                    switch = guess
                    last = line[i+1:]
                    line = first + switch + last
            if count > 0:
                print('You are correct!')
                count = 0
                print('The word looks like: ' + line)
                print('You have ' + str(life) + ' guesses left.')
            else:
                print('There is no '+str(guess)+'\'s in the word')
                life -= 1  # if players make the wrong guess, one chance of guesses is decreased
                print('The word looks like: ' + line)
                print('You have ' + str(life) + ' guesses left.')
            if line.find('-') == -1:
                print('You win!!\nThe word was :'+str(word))
                break
            if life == 0:
                print('You are completely hung : (\nThe word was : '+str(word))
                break






def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

