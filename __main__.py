#!/usr/bin/env python3

import argparse
from smartsnek import Word

def main():
    parser = argparse.ArgumentParser(description="Search definition(s) of a word.")
    parser.add_argument('word', help='search definition of this word')
    parser.add_argument('-q', '--quantity', type=int, help='number of results to return')
    args = parser.parse_args()
    word = Word(args.word)
    if args.quantity:
        word = Word(args.word, quantity=args.quantity)
    else:
        word = Word(args.word)
    print(word)

if __name__ == "__main__":
    main()
