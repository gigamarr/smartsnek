#!/usr/bin/env python3

import argparse
from smartsnek import Word

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='search definition of this word')
    args = parser.parse_args()
    word = Word(args.word)
    print(word)

if __name__ == "__main__":
    main()
