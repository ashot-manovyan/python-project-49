import prompt
import random


def task():
    number = random.choice(range(1000))
    answer = prompt.string(f'Question: {number}\nYour answer: ')
    correct_answer = 'Yes' if number % 2 == 0 else 'No'
    return (answer.lower(), correct_answer.lower())
