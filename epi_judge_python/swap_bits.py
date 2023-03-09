from test_framework import generic_test


def swap_bits(x, i, j):
    iBit = (x >> i) & 1
    jBit = (x >> j) & 1
    if iBit == jBit:
        return x

    mask = (1 << i) | (1 << j)
    return x ^ mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
