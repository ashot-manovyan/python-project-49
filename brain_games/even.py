import prompt


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def question(number):
    if is_even(number):
        correct_answer = 'Yes'
    else:
        correct_answer = 'No'
    answer = prompt.string(f'Question: {number}\nYour answer: ')
    if answer.lower() == correct_answer.lower():
        result = 'Correct'
        print('Correct!')
    else:
        result = 'Wrong'
        print(f"'{answer}' is a wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")
    return result


def quiz(source):
    counter = 0
    for i in source:
        if question(i) == 'Wrong':
            break
        else:
            counter += 1
    return counter
