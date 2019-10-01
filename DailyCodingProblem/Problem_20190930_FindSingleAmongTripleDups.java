/**
 * This problem was asked by Google.
 * 
 * Given an array of integers where every integer occurs three times except for
 * one integer, which only occurs once, find and return the non-duplicated
 * integer.
 * 
 * For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
 * return 19.
 * 
 * Do this in O(N) time and O(1) space.
 */

 /**
  * Idea is to get each bit one at a time. For each position from 0 to 64, add all this position's bit
  * together and get its modular 3. That's the bit for the same position of the final result.
  */
 class FindSingleAmongTripleDups {
     public static void main(String[] args) {
         int[] a1 = {6, 1, 3, 3, 3, 6, 6};
         int[] a2 = {13, 19, 13, 13};
         System.out.println(FindSingleAmongTripleDups.findSingle(a1));
         System.out.println(FindSingleAmongTripleDups.findSingle(a2));
     }

     // assume the input is always valid
     public static int findSingle(int[] input) {
         int result = 0;
         int[] sum = new int[64];
        for (int i = 0; i < input.length; i++) {
            for (int j=0; j<64; j++) {
                // sum[j] is the sum of the jth position
                sum[j] +=  ((input[i] >> j) & 1);
            }
        }
        for (int i = 0; i < 64; i++) {
            sum[i] = sum[i] % 3;
            if (sum[i] > 1) throw new IllegalStateException();
            result = result | (sum[i] << i);
        }
        return result;
    }
 }