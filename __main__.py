#!/usr/bin/env python3

import sys
import argparse
from smartsnek import Word

def main():
    parser = argparse.ArgumentParser(description='Search definition(s) of a word.')
    parser.add_argument('word', help='search definition of this word')
    parser.add_argument('-c', '--count', type=int, help='number of results to return')
    parser.add_argument('-s', '--silent', action='store_true', help='silence output of the definitions')
    parser.add_argument('-w', '--write', action='store_true', help='write the output to a file')
    parser.add_argument('-i', '--index', type=int, help='specify index of the item to write to the file (used with [ -w | --write ])')
    args = parser.parse_args()


    if args.count:
        word = Word(args.word, count=args.count)
    else:
        word = Word(args.word)

    if args.write:
        if args.index:
            try:
                word.write("{} - {} ({}) - [\n{} ]\n\n".format(word, word.pronunciation, word.word_type, word.definitions[args.index-1]))
            except IndexError:
                print("Definition with given index not found.")
                sys.exit()
        else:
            word.write("{} - {} ({}) - [\n{} ]\n\n".format(word, word.pronunciation, word.word_type, ''.join(word.definitions)))

    if not args.silent:
        print(word.representation)

if __name__ == '__main__':
    main()
