#!/usr/bin/env python3

import argparse
from smartsnek import Word

def main():
    parser = argparse.ArgumentParser(description="Search definition(s) of a word.")
    parser.add_argument('word', help='search definition of this word')
    parser.add_argument('-c', '--count', type=int, help='number of results to return')
    parser.add_argument('-s', '--silent', action="store_true", help="silence output of the definitions")
    args = parser.parse_args()


    if args.count:
        word = Word(args.word, count=args.count)
    else:
        word = Word(args.word)

    if not args.silent:
        print(word)

if __name__ == "__main__":
    main()
