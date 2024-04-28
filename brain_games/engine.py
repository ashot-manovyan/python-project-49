import brain_games.greetings


name = brain_games.greetings.name


def quiz(func):
    score = 0
    for i in range(3):
        user_answer, system_answer = func()
        if user_answer == system_answer:
            print("Correct!")
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{system_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    if score == 3:
        print(f'Congratulations, {name}!')
