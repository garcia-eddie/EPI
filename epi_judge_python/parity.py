from test_framework import generic_test


def parity(x: int) -> int:
    bit = 0
    while x != 0:
        x = x & (x - 1)
        bit ^= 1
    return bit


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
