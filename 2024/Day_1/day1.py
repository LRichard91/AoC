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
    
    listA: list[int] = []
    listB: list[int] = []
    
    for item in rawInput:
        splitLine = item.split("   ")
        listA.append(int(splitLine[0]))
        listB.append(int(splitLine[1]))

    listA.sort()
    listB.sort()

    if debug:
        print('The separate lists, sorted in ascending order:\n')
        pprint(listA)
        pprint(listB)
        print('')

    for idx, _ in enumerate(listA):
        parsed_input.append((listA[idx], listB[idx]))

    return parsed_input


def part_1(input, debug=False):
    '''Solve Part 1'''
    totalDistance: int = 0
    for item in input:
        totalDistance += abs(item[0] - item[1])

    return totalDistance


def part_2(input, debug=False):
    '''Solve Part 2'''
    similarityScore: int = 0
    listOfTotals: list[int] = []

    leftList: list[int] = []
    rightList: list[int] = []

    for item in input:
        leftList.append(item[0])
        rightList.append(item[1])

    if debug:
        print('The left list:', leftList, '\n')
        print('The right list:', rightList, '\n')

    for leftValue in leftList:
        count = 0
        for rightValue in rightList:
            if rightValue == leftValue:
                count += 1
        listOfTotals.append(leftValue * count)

    similarityScore = sum(listOfTotals)
    return similarityScore


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
