#!/usr/bin/env python3
import brain_games.greetings
import brain_games.engine
import brain_games.games.progression


def main():
    brain_games.greetings
    print('What number is missing in the progression?')
    brain_games.engine.quiz(brain_games.games.progression.task)


if __name__ == '__main__':
    main()
