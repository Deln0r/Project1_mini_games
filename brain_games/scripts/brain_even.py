#!/usr/bin/env python3
from random import randint
import prompt


def game_1():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def questions():
        count = 0
        while count < 3:
            number = randint(1, 100)
            print(f'Question: {number}')
            answer = prompt.string('Your answer: ')
            if answer == is_even(number):
                print('Correct!')
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(number)}'.")
                print(f"Let's try again, {name}!")
                break
        if count == 3:
            print(f'Congratulations, {name}!')
    questions()


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    print('Welcome to the Brain Games!')
    game_1()


if __name__ == '__main__':
    main()
