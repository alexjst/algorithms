package alexyang.algorithms.Java.src;

/**
 * Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

 */
public class SingleNumber {
    public static void main(String[] args) {
        int[] arr = {2,2,1, 6, 6, 7, 9, 7, 1};
        System.out.println(findSingleNum(arr));
    }

    private static int findSingleNum(int[] arr) {
        int result = arr[0];
        for (int i=1; i<arr.length; i++) {
            result ^= arr[i];
        }
        return result;
    }
}