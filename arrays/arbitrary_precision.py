"""
A program which takes as input an array of digits encoding
a decimal integer D and updates the array to represent the
integer D + 1.

Example: If the input is <1, 2, 9>, then the array should be
updated to <1, 3, 0>.
"""


def brute_plus_one(l):
    num = int(''.join(str(x) for x in l)) + 1
    return list(int(x) for x in str(num))


if __name__ == '__main__':
    assert(brute_plus_one([1, 2, 3]) == [1, 2, 4])
    assert(brute_plus_one([1, 2, 9]) == [1, 3, 0])
    assert(brute_plus_one([9, 9, 9]) == [1, 0, 0, 0])
