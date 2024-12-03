#!/usr/bin/env python

import argparse
from pprint import pprint
import re
import sys


def parse_input(filename, debug=False):
    '''Parse the input file'''
    parsed_input = []
    with open(filename, "r") as inputFile:
        rawInput = inputFile.read().strip('\n')

    if debug:
        print('The raw input:\n')
        print(rawInput)
        print('')

    parsed_input.append(rawInput)

    return parsed_input


def part_1(input, debug=False):
    '''Solve Part 1'''

    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)", re.IGNORECASE)
    matched = pattern.findall(input[0])

    toMultiply: list[tuple[int, int]] = []

    if debug:
        print(matched)
        print('')

    for item in matched:
        item = item[4 : len(item) - 1]
        splitItem = item.split(',')
        toMultiply.append((int(splitItem[0]), int(splitItem[1])))

    if debug:
        print(toMultiply)

    multipliedList = [x[0] * x[1] for x in toMultiply]

    if debug:
        print(multipliedList)

    return sum(multipliedList)


def part_2(input, debug=False):
    '''Solve Part 2'''
    patternMul = re.compile(r"mul\(\d{1,3},\d{1,3}\)", re.IGNORECASE)
    patternDo = re.compile(r"do\(\)", re.IGNORECASE)
    patternDont = re.compile(r"don\'t\(\)", re.IGNORECASE)

    if debug:
        print(patternMul.findall(input[0]))
        print(patternDo.search(input[0]).span())
        print(patternDont.search(input[0]).span())

    fullString = input[0]
    toMultiply: list[tuple[int, int]] = []
    
    conditionalSpan: tuple[int, int] = patternDont.search(fullString).span()
    subString: str = fullString[:conditionalSpan[1]]

    

    return 0


def main():
    '''Main function'''
    arg_parser = argparse.ArgumentParser(
        description='Solves the puzzles for the given day of AOC'
    )
    arg_parser.add_argument(
        'filename', 
        help='The path to the input file'
    )
    arg_parser.add_argument(
        '-d',
        '--debug',
        dest='debug',
        action='store_true',
        help='Enables debug messages'
    )
    arg_parser.add_argument(
        '-1',
        '--part1',
        dest='part1',
        action='store_true',
        help='Executes the solution for Part 1'
    )
    arg_parser.add_argument(
        '-2',
        '--part2',
        dest='part2',
        action='store_true',
        help='Executes the solution for Part 2'
    )
    args = arg_parser.parse_args()

    if args.debug:
        print('')
        print('Debug messages are ON')
        print('')

    parsed_input = parse_input(args.filename, args.debug)

    if args.debug:
        print('The parsed input:')
        print('')
        pprint(parsed_input)
        print('')        

    if args.part1 and args.debug:
        print('======================================================')
        print('                        Part 1                        ')
        print('======================================================')
        print('')

    if args.part1:
        solution_1 = part_1(parsed_input, args.debug)
        print('')
        print('The solution for Part 1 is:', solution_1)
        print('')

    if args.part2 and args.debug:
        print('======================================================')
        print('                        Part 2                        ')
        print('======================================================')
        print('')

    if args.part2:
        solution_2 = part_2(parsed_input, args.debug)
        print('')
        print('The solution for Part 2 is', solution_2)
        print('')
        
    sys.exit(0)


if __name__ == "__main__":
    main()
