/**
 * This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
 */

class Problem_20190825_MissingInteger {
    public static void main(String[] args) {
        System.out.println(findMissingInteger(new int[] { 3, 4, -1, 1 }));
        System.out.println(findMissingInteger(new int[] { 1, 2, 0 }));
        System.out.println(findMissingInteger(new int[] { 2, 1, 0,-4,-5,3,6,8,2,-1}));
    }

    public static int findMissingInteger(int[] input) {
        int len = input.length;
        if (input == null || len == 0)
            return -1;

        for (int i = 0; i < len; i++) {
            int num = input[i];
            while (num>=1 && num<=len && num != input[num-1]) {
                int next = input[num-1];
                input[num-1] = num;
                num = next;
            }
        }
        for (int i = 0; i < len; i++) {
            if (input[i] != (i+1)) {
                return i+1;
            }
        }

        return 0;
    }
}