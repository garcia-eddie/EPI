from test_framework import generic_test


def count_bits(x: int) -> int:
    bits = 0
    while x:
        x = x & (x - 1)
        bits += 1

    return bits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
