from test_framework import generic_test


def reverse_bits(x: int) -> int:
    bitmask = 0xFFFF
    firstQuarter = reverse((x >> 48) & bitmask)
    secondQuarter = reverse((x >> 32) & bitmask)
    thirdQuarter = reverse((x >> 16) & bitmask)
    fourthQuarter = reverse(x & bitmask)

    return firstQuarter | (secondQuarter << 16) | (thirdQuarter << 32) | (fourthQuarter << 48)

def reverse(x: int) -> int:
    x = (x >> 8) | (x << 8)
    x = (x & 0xF0F0) >> 4 | (x & 0x0F0F) << 4
    x = (x & 0xCCCC) >> 2 | (x & 0x3333) << 2
    x = (x & 0xAAAA) >> 1 | (x & 0x5555) << 1
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
