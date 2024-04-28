#!/usr/bin/env python3
import brain_games.greetings
import brain_games.engine
import brain_games.games.even


def main():
    brain_games.greetings
    print('Answer "yes" if number is even, otherwise answer "no".')
    brain_games.engine.quiz(brain_games.games.even.task)


if __name__ == '__main__':
    main()
