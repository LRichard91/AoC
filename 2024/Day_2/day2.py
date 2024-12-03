#!/usr/bin/env python

import argparse
from pprint import pprint
import sys


def parse_input(filename, debug=False):
    '''Parse the input file'''
    parsed_input = []
    with open(filename, "r") as inputFile:
        rawInput: list[str] = inputFile.read().splitlines()

    if debug:
        print('The raw input:\n')
        pprint(rawInput)
        print('')

    for item in rawInput:
        items = item.split(" ")
        
        if debug:
            print('Numbers:', items, '\n')
        
        intList = [int(x) for x in items]
        parsed_input.append(intList)

    return parsed_input


def part_1(input, debug=False):
    '''Solve Part 1'''
    safeReports: int = 0

    for lst in input:
        safe: bool = True
        ascending: bool = False
        descending: bool = False

        for idx, _ in enumerate(lst):
            if idx == 0:
                if lst[idx] < lst[idx + 1]:
                    ascending = True
                elif lst[idx] > lst[idx + 1]:
                    descending = True
                else:
                    safe = False
                    break
            elif safe:
                if lst[idx] == lst[idx - 1]:
                    safe = False
                    break
                if abs(lst[idx] - lst[idx - 1]) > 3:
                    safe = False
                    break
                if ascending and lst[idx] < lst[idx - 1]:
                    safe = False
                    break
                if descending and lst[idx] > lst[idx - 1]:
                    safe = False
                    break
            else:
                break
        
        if safe:
            safeReports += 1

    return safeReports


def part_2(input, debug=False):
    '''Solve Part 2'''
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
