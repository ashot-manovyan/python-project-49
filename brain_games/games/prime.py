import prompt
import random


def is_prime(num):
    if num == 0 or num == 1:
        return "no"
    elif num == 2:
        return "yes"
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return "no"
        i += 1
    return "yes"


def task():
    number = random.randint(0, 100)
    answer = prompt.string("Question: {}\n"
                           "Your answer: ".format(number))
    correct_answer = is_prime(number)
    return (answer.lower(), correct_answer.lower())
