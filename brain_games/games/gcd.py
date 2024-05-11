import prompt
import random


def gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    remainder = num1 % num2
    while remainder != 0:
        num1 = remainder
        remainder = num2 % remainder
        num2 = num1
    else:
        return num2


def task():
    a = random.randint(0, 30)
    b = random.randint(0, 30)
    answer = prompt.string("Question: {} {}\n"
                               "Your answer: ".format(a, b))
    correct_answer = str(gcd(a, b))
    return (answer, correct_answer)
