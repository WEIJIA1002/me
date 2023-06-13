# -*- coding: UTF-8 -*-
"""Modify each function until the tests pass."""


def is_odd(a_number):
    """Return True if a_number is odd, and False if a_number is even."""
    return a_number % 2 != 0


def fix_it(moves=True, should_move=True):
    """Decide what to do."""
    if moves == True and should_move == False:
        return "Duct Tape"
    if moves == False and should_move == True:
        return("WD-40")       
    else:        
        return("No Problem")


def loops_preview():
    """Make 8 poops."""
    choc_list = []
    for _ in range(8):
        choc_list.append("💩")
    return choc_list


def loops_1a():
    """Make 10 stars."""
    star_list = []
    for _ in range(10):
        star_list.append("*")
    return star_list


def loops_1c(number_of_items=5, symbol="#"):
    """Respond to variables."""
    symbol_list = []
    for _ in range(number_of_items):
        symbol_list.append(symbol)
    return symbol_list


def loops_2():
    """Make a big square starfield."""
    starfield = []
    for _ in range(10):
        row = []
        for _ in range(10):
            row.append("*")
        starfield.append(row)
    return starfield


def loops_3():
    """Make a rising block of numbers."""
    number_block = []
    for i in range(10):
        row = []
        for _ in range(10):
            row.append(str(i))
        number_block.append(row)
    return number_block


def loops_4():
    """Make a block of numbers that rises left to right."""
    number_block = []
    for _ in range(10):
        row = []
        for i in range(10):
            row.append(str(i))
        number_block.append(row)
    return number_block


def loops_5():
    """Make the coordinates of the block."""
    coordinate_block = []
    for i in range(10):
        row = []
        for j in range(5):
            row.append(f"(i{i}, j{j})")
        coordinate_block.append(row)
    return coordinate_block


def loops_6():
    """Make a wedge of numbers."""
    wedge = []
    for i in range(10):
        row = []
        for j in range(i + 1):
            row.append(str(j))
        wedge.append(row)
    return wedge


def loops_7():
    """Make a pyramid."""
    pyramid = []
    for i in range(5):
        row = []
        for _ in range(4 - i):
            row.append(" ")
        for _ in range(2 * i + 1):
            row.append("*")
        for _ in range(4 - i):
            row.append(" ")
        pyramid.append(row)
    return pyramid


def little_printer(some_kind_of_list, exercise_name):
    """Help to see what's going on."""
    print("\n🔎 " + exercise_name)
    if some_kind_of_list is not None:
        for row in some_kind_of_list:
            print(row)
    else:
        print("\tMaybe you haven't got to this one yet?")


if __name__ == "__main__":
    # Add function calls and tests here
    # Test is_odd function
    print(is_odd(3))  # Expected output: True
    print(is_odd(4))  # Expected output: False

    # Test fix_it function
    print(fix_it(True, True))   # Expected output: "No Problem"
    print(fix_it(True, False))  # Expected output: "WD-40"
    print(fix_it(False, True))  # Expected output: "Duct Tape"
    print(fix_it(False, False)) # Expected output: "No Problem"

    # Test loops_preview function
    print(loops_preview())  # Expected output: ['💩', '💩', '💩', '💩', '💩', '💩', '💩', '💩']

    # Test loops_1a function
    print(loops_1a())  # Expected output: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

    # Test loops_1c function
    print(loops_1c(5, "#"))  # Expected output: ['#', '#', '#', '#', '#']
    print(loops_1c(3, "*"))  # Expected output: ['*', '*', '*']

    # Test loops_2 function
    starfield = loops_2()
    for row in starfield:
        print(row)  # Expected output: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

    # Test loops_3 function
    number_block = loops_3()
    for row in number_block:
        print(row)  # Expected output: ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

    # Test loops_4 function
    number_block = loops_4()
    for row in number_block:
        print(row)  # Expected output: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Test loops_5 function
    coordinate_block = loops_5()
    for row in coordinate_block:
        print(row)  # Expected output: ['(i0, j0)', '(i0, j1)', '(i0, j2)', '(i0, j3)', '(i0, j4)']

    # Test loops_6 function
    wedge = loops_6()
    for row in wedge:
        print(row)  # Expected output: ['0'], ['0', '1'], ['0', '1', '2'], ..., ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Test loops_7 function
    pyramid = loops_7()
    for row in pyramid:
        print(row)  # Expected output: [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '], ..., ['*', '*', '*', '*', '*', '*', '*', '*', '*']

