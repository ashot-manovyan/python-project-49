import prompt
import random


def task():
    a = random.randint(0, 30)
    len = random.randint(5, 10)
    index = random.randint(0, len - 1)
    increment = random.randint(2, 8)
    list = [a]
    for i in range(len - 1):
        list.append(list[i] + increment)
    question_list = list[:]
    question_list[index] = '..'
    string = ' '.join(map(str, question_list))
    answer = prompt.string("Question: {}\n"
                           "Your answer: ".format(string))
    correct_answer = str(list[index])
    return (answer, correct_answer)
