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
    parser.add_argument('-i', '--index', type=int, nargs='+', help='specify index of the item to write to the file (used with [ -w | --write ])')
    args = parser.parse_args()


    if args.count:
        word = Word(args.word, count=args.count)
    else:
        word = Word(args.word)

    if args.write:
        if args.index:
            try:
                definitions = ""
                for index in args.index:
                    definitions += word.definitions[index-1] 
                word.write("{} - {} ({}) - [\n{} ]\n\n".format(word, word.pronunciation, word.word_type, definitions))
            except IndexError:
                print("Definition with given index not found.")
                sys.exit()
        else:
            word.write("{} - {} ({}) - [\n{} ]\n\n".format(word, word.pronunciation, word.word_type, ''.join(word.definitions)))

    if not args.silent:
        print(word.representation)

if __name__ == '__main__':
    main()
