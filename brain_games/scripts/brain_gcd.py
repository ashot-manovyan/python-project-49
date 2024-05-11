#!/usr/bin/env python3
import brain_games.greetings
import brain_games.engine
import brain_games.games.gcd


def main():
    brain_games.greetings
    print('Find the greatest common divisor of given numbers.')
    brain_games.engine.quiz(brain_games.games.gcd.task)


if __name__ == '__main__':
    main()
