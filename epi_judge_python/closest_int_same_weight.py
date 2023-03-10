from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    """
    The weight of a nonnegative integer x is the number of bits that are set to 1 in its 
    binary representation. For example, 92 in base-2 is 0x01011100, so its weight is 4.

    Write a program that takes as input a nonnegative integer x and returns a number y 
    which is not equal  to x, but has the same weight as x and their difference |y - x| 
    is as small as possible. Assume the integer fits in 64 bits.
    """
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if ((x >> i) & 1) != ((x >> i + 1) & 1):
            mask = (1 << i) | (1 << (i + 1))
            return x ^ mask

    return ValueError('All bits are 0 or 1')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
