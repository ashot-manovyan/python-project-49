#!/usr/bin/env python3
import brain_games.greetings
import brain_games.engine
import brain_games.games.calc


def main():
    brain_games.greetings
    print('What is the result of the expession?')
    brain_games.engine.quiz(brain_games.games.calc.task)


if __name__ == '__main__':
    main()
