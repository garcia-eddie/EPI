package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class PrimitiveDivide {
  @EpiTest(testDataFile = "primitive_divide.tsv")
  public static int divide(int x, int y) {
    int res = 0;
    while (x >= y) {
      int shift = 0;
      long yPower = y;
      while (x >= (yPower << shift)) {
        shift++;
      }
      shift--;
      res += 1 << shift;
      x -= y << shift;
    }

    return res;
  }

  public static void main(String[] args) {
    int res = divide(2097428739, 186);
    System.exit(
        GenericTest
            .runFromAnnotations(args, "PrimitiveDivide.java",
                new Object() {
                }.getClass().getEnclosingClass())
            .ordinal());
  }
}
