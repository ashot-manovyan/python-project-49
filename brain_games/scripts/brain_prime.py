#!/usr/bin/env python3
import brain_games.greetings
import brain_games.engine
import brain_games.games.prime


def main():
    brain_games.greetings
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    brain_games.engine.quiz(brain_games.games.prime.task)


if __name__ == '__main__':
    main()
