import java.util.*;

/**
 * Good morning! Here's your coding interview problem for today.
 *
 * This problem was recently asked by Google.
 *
 * Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
 *
 * For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
 *
 * Bonus: Can you do this in one pass?
 */

public class Problem_20190822_TwoSumOnePass {

    public static void main(String[] args) {
        // write your code here
        int[] input = new int[]{10, 15, 3, 7};
        System.out.println(hasSum(input, 17));
        System.out.println(hasSum(input, 18));
        System.out.println(hasSum(input, 27));
    }

    private static boolean hasSum(int[] input, int k) {
        int len = input.length;
        if (input == null || len == 0) return false;
        Map<Integer, Integer> val2PosMap = new HashMap<>();
        for (int i = 0; i < len; i++) {
            int target = k - input[i];
            if (val2PosMap.containsKey(target) && val2PosMap.get(target) != i) {
                return true;
            }
            val2PosMap.put(input[i], i);
        }
        return false;

    }



}

