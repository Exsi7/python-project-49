#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.is_even import is_even


def main():
    engine_game(is_even)


if __name__ == '__main__':
    main()
