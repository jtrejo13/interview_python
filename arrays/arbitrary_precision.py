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


def plus_one(l):
    # starting at the back increase number by one
    # if number increased is equal to 10, change to 0
    # continue until begining of string is reached or number isn't equal to 10
    # Finally, if begining of array is equal to 0. Insert a 1 at beginning
    for i in range(len(l)):
        l[~i] += 1
        if l[~i] == 10:
            l[~i] = 0
        else:
            break
        if l[0] == 0:
            l.insert(0, 1)
    return l


if __name__ == '__main__':

    fail_test = lambda: print('Fail')
    pass_test = lambda: print('Pass')

    pass_test() if brute_plus_one([1, 2, 3]) == [1, 2, 4] else fail_test()
    pass_test() if brute_plus_one([1, 2, 9]) == [1, 3, 0] else fail_test()
    pass_test() if brute_plus_one([8, 9, 9]) == [9, 0, 0] else fail_test()
    pass_test() if brute_plus_one([9, 9, 9]) == [1, 0, 0, 0] else fail_test()

    pass_test() if plus_one([1, 2, 3]) == [1, 2, 4] else fail_test()
    pass_test() if plus_one([1, 2, 9]) == [1, 3, 0] else fail_test()
    pass_test() if plus_one([8, 9, 9]) == [9, 0, 0] else fail_test()
    pass_test() if plus_one([9, 9, 9]) == [1, 0, 0, 0] else fail_test()
    
