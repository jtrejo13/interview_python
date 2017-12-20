"""
A program that takes two arrays representing integers, and
returns an integer representing their product.

Example: since 193707721 * -761838257287 = -147573952589676412927,
if the inputs are <1,9,3,7,0,7,7,2,1> and <-7,6,1,8,3,8,2,5,7,2,8,7>,
the function should return <-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7>
"""


def brute_mult(A, B):
    num_a = int(''.join([str(a) for a in A]))
    num_b = int(''.join([str(b) for b in B]))
    ans = num_a * num_b
    result = [int(i) for i in str(abs(ans)) if type(i)]
    if ans < 0:
        result[0] *= -1
    return result


def multiply(A, B):
    pass
    # multiply [ai] * [bj]
    # carry over when == 10
    # sum results
    ans = []
    count = 0
    for i in reversed(range(len(A))):
        num = []
        for j in reversed(range(len(B))):
            mul = A[i] * B[j]
            num.insert(0, mul)
        ans.append(num)
    print(ans)


if __name__ == '__main__':
    failed = lambda: print('Fail')
    passed = lambda: print('Pass')

    passed() if brute_mult([2], [3]) == [6] else failed()
    passed() if brute_mult([1, 2, 3], [-2]) == [-2, 4, 6] else failed()
    passed() if brute_mult([1, 2, 3], [2, 2, 2]) == [2, 7, 3, 0, 6] \
                               else failed()
    passed() if brute_mult(
        [1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]) \
        == [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7] \
        else failed()

    passed() if multiply([2], [3]) == [6] else failed()
    passed() if multiply([1, 2], [2]) == [2, 4] else failed()
    passed() if multiply([1, 2], [2, 4]) == [2, 8, 8] else failed()
    passed() if False else failed()
