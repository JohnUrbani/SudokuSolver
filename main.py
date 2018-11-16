# John Urbani
# CS21
# Final Project: Sudoku Game with hint giving and auto solving.
# Puzzles stored in 9 x 9 csv files that show blank spaces as 0's

import os
import sys
sys.setrecursionlimit(10000)


# Main game loop
def main():
    option = input('Choose an option: [u]pload puzzle, [r]andom puzzle, [s]olve puzzle, [v]iew puzzle, [e]xit: ')
    puzzles = os.listdir('puzzles')
    if option == 'u':
        upload(open('puzzles/' + puzzles[choose_file(puzzles)], 'r'))

    if option == 's':
        solve_file(open('puzzles/' + puzzles[choose_file(puzzles)], 'r'))

    if option == 'v':
        view(open('puzzles/' + puzzles[choose_file(puzzles)], 'r'))


def choose_file(puzzles_list):
    print('Here are your choices:')
    for i in range(len(puzzles_list)):
        print(i + 1, ': ', puzzles_list[i], sep='')
    file_index = int(input('Please select a file (1 - ' + str(len(puzzles_list)) + '): ')) - 1
    if 0 <= file_index < len(puzzles_list):
        return file_index


def upload(csv):
    print(1+1)


def solve_file(csv):
    values = csv.read().replace('\n', ',').split(',')

    # Testing 1 index
    print(get_related_positions(values, 0))
    print()

    for i in range(len(values)):
        print(get_related_positions(values, i))


# Find all positions related to the given index
def get_related_positions(vals, i):
    related_positions = [i]
    related_positions.extend(get_inline_positions(vals, i))
    related_positions.extend(get_grid_positions(vals, i))
    # Remove crossover values
    return list(set(related_positions))


# Find all positions up, down, left, and right from the index in the 9x9 grid
def get_inline_positions(vals, i):
    inline_positions = []
    up = i - 9
    down = i + 9
    left = i
    right = i + 1

    if i >= 0 <= 80:
        while up >= 0:
            inline_positions.append(up)
            up -= 9

        while down <= 80:
            inline_positions.append(down)
            down += 9

        while left % 9 != 0:
            left -= 1
            inline_positions.append(left)

        while right % 9 != 0:
            inline_positions.append(right)
            right += 1

        return inline_positions


# Find and return the list of locations in a certain grid
def get_locations_in_grid(grid):
    locations = []
    if grid == 1:
        locations.extend(list(range(0, 3)))
        locations.extend(list(range(9, 12)))
        locations.extend(list(range(18, 21)))
        return locations
    elif grid == 2:
        locations.extend(list(range(3, 6)))
        locations.extend(list(range(12, 15)))
        locations.extend(list(range(21, 24)))
        return locations
    elif grid == 3:
        locations.extend(list(range(6, 9)))
        locations.extend(list(range(15, 18)))
        locations.extend(list(range(24, 27)))
        return locations
    elif grid == 4:
        locations.extend(list(range(27, 30)))
        locations.extend(list(range(36, 39)))
        locations.extend(list(range(45, 48)))
        return locations
    elif grid == 5:
        locations.extend(list(range(30, 33)))
        locations.extend(list(range(39, 42)))
        locations.extend(list(range(48, 51)))
        return locations
    elif grid == 6:
        locations.extend(list(range(33, 36)))
        locations.extend(list(range(42, 45)))
        locations.extend(list(range(51, 54)))
        return locations
    elif grid == 7:
        locations.extend(list(range(54, 57)))
        locations.extend(list(range(63, 66)))
        locations.extend(list(range(72, 75)))
        return locations
    elif grid == 8:
        locations.extend(list(range(57, 60)))
        locations.extend(list(range(66, 69)))
        locations.extend(list(range(75, 78)))
        return locations
    elif grid == 9:
        locations.extend(list(range(60, 63)))
        locations.extend(list(range(69, 72)))
        locations.extend(list(range(78, 81)))
        return locations
    else:
        return locations


# Find all positions in relation to the index in its 3x3 grid
def get_grid_positions(vals, i):
    grid_positions = []
    grid = 0
    for j in range(3):
        if 0+(3*j) <= i < 3+(3*j) or 9+(3*j) <= i < 12+(3*j) or 18+(3*j) <= i < 21+(3*j):
            grid = j+1
        elif 27 + (3 * j) <= i < 30 + (3 * j) or 36 + (3 * j) <= i < 39 + (3 * j) or 45 + (3 * j) <= i < 48 + (3 * j):
            grid = j + 4
        elif 54 + (3 * j) <= i < 57 + (3 * j) or 63 + (3 * j) <= i < 66 + (3 * j) or 72 + (3 * j) <= i < 75 + (3 * j):
            grid = j + 7

    grid_positions.extend(get_locations_in_grid(grid))

    return grid_positions


def view(csv):
    for line in csv.readlines():
        single_list = line.rstrip().replace('0', ' ').split(',')
        # print('-------------------------------------')
        print('|', end='')
        for single in single_list:
            print('', single, '', end='|')
        print()
    # print('-------------------------------------')
    main()


main()
