package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class PrimitiveMultiply {
  @EpiTest(testDataFile = "primitive_multiply.tsv")
  public static long multiply(long x, long y) {
    if (x == 0 || y == 0) {
      return 0;
    }

    long sum = 0;
    while (y != 0) {
      if ((y & 1) == 1) {
        sum = primitiveAdd(sum, x);
      }
      x <<= 1;
      y >>>= 1;
    }

    return sum;
  }

  public static long primitiveAdd(long x, long y) {
    while (y != 0) {
      long carry = x & y;
      long diff = x ^ y;
      x = (carry << 1) | diff;
      y = (carry << 1) & diff;
    }

    return x;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "PrimitiveMultiply.java",
                new Object() {
                }.getClass().getEnclosingClass())
            .ordinal());
  }
}
