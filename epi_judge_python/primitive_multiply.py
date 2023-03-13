from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    sum = 0
    while y != 0:
        if y & 1:
            sum = add(sum, x)
        x <<= 1
        y >>= 1
    return sum


def add(x: int, y: int) -> int:
    while y != 0:
        shift = x & y
        carry = x ^ y
        x = (shift << 1) | carry
        y = (shift << 1) & carry

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
