from test_framework import generic_test


def divide(x: int, y: int) -> int:
    res = 0
    while x >= y:
        shift = 1
        while x >= (y << shift):
            shift += 1
        shift -= 1
        res += (1 << shift)
        x -= (y << shift)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
