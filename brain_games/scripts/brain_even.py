#!/usr/bin/env python3
import prompt
import random
import brain_games.even


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "Yes" if number is even, otherwise answer "No"')
    question_numbers = random.sample(range(0, 1000), 3)
    if brain_games.even.quiz(question_numbers) == len(question_numbers):
        print(f'Congratilations, {name}!')


if __name__ == '__main__':
    main()
