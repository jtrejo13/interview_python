"""
A program that takes two arrays representing integers, and
returns an integer representing their product.

Example: since 193707721 * -761838257287 = -147573952589676412927,
if the inputs are <1,9,3,7,0,7,7,2,1> and <-7,6,1,8,3,8,2,5,7,2,8,7>,
the function should return <-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7>
"""


# bute force might overflow
def brute_mult(A, B):
    num_a = int(''.join([str(a) for a in A]))
    num_b = int(''.join([str(b) for b in B]))
    ans = num_a * num_b
    result = [int(i) for i in str(abs(ans)) if type(i)]
    if ans < 0:
        result[0] *= -1
    return result


def multiply(A, B):
    # absolute value of A and B
    sign = -1 if A[0] * B[0] < 0 else 1
    A[0], B[0] = abs(A[0]), abs(B[0])

    # multiply [ai] * [bj]
    # carry over when == 10
    res = [0] * (len(A) + len(B))
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            res[i + j + 1] += A[i] * B[j]
            res[i + j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10

    # remove leading zeros
    while res[0] == 0:
        res.pop(0)
    # update sign
    res[0] = sign * res[0]

    return res


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
    passed() if multiply([1, 2, 3], [-2]) == [-2, 4, 6] else failed()
    passed() if multiply([1, 2, 3], [2, 2, 2]) == [2, 7, 3, 0, 6] \
                               else failed()
    passed() if multiply(
        [1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]) \
        == [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7] \
        else failed()
