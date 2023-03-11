package epi_judge_variants;

public class variants_4_1 {
    /*
     * Given a number x, right propagate the
     * rightmost set bit.
     * 
     * Example:
     * 01010000 -> 01011111
     */
    public static long rightPropagate(long x) {
        if (x == 0) {
            return x;
        }
        return x | (x - 1);
    }

    /*
     * Given a number x and a power of two powTwo,
     * return the result of x mod powTwo.
     * 
     * Example:
     * 77 mod 64 -> 13
     */
    public static long xModPowerOfTwo(long x, long powTwo) {
        if (x < powTwo) {
            return x;
        }

        int highestBit = (int) (Math.log(powTwo) / Math.log(2));
        long mask = (x >>> highestBit) << highestBit;

        return x ^ mask;
    }

    public static boolean powerOfTwo(long x) {
        int highestBit = (int) (Math.log(x) / Math.log(2));
        long mask = 1L << highestBit;

        return (x & mask) == 0;
    }

    public static void main(String[] args) {

    }
}
