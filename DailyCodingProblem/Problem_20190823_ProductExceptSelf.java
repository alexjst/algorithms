/**
 * This problem was asked by Uber.
 * 
 * Given an array of integers, return a new array such that each element at
 * index i of the new array is the product of all the numbers in the original
 * array except the one at i.
 * 
 * For example, if our input was [1, 2, 3, 4, 5], the expected output would be
 * [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
 * be [2, 3, 6].
 * 
 * Follow-up: what if you can't use division?
 */

class Problem_20190823_ProductExceptSelf {

    public static void main(String[] args) {
        int[] input = new int[]{1,2,3,4};
        int[] output = getProductExceptSelfArray(input);
        for (int i : output) {
            System.out.print(i + "\t");
        }
        System.out.println();
    }

    public static int[] getProductExceptSelfArray(int[] input) {
        // using division is actually not trivial, when you have to consider the case of '0' appearances
        if (input == null || input.length == 0) return input;
        int len = input.length;
        int[] left = new int[len];
        int[] right = new int[len];
        for (int i=0; i<len; i++) {
            if (i==0) left[i] = 1;
            else left[i] = left[i-1] * input[i-1];
        }
        for (int i=len-1; i>=0; i--) {
            if (i==len-1) right[i] = 1;
            else right[i] = right[i+1] * input[i+1];
        }
        for (int i=0; i<len; i++) {
            right[i] *= left[i];
        }
        return right;
    }
}