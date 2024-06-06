import prompt
import operator
import random


operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]


def task():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op, fn = random.choice(operators)
    answer = prompt.string("Question: {} {} {}?\n"
                           "Your answer: ".format(a, op, b))
    correct_answer = str(fn(a, b))
    return (answer, correct_answer)
