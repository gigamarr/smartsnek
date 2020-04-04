#!/usr/bin/env python3

import sys
from smartsnek import Word

def main():
    try:
        word = Word(sys.argv[1])
        print(word)
    except IndexError:
        print("No word provided")

if __name__ == "__main__":
    main()
